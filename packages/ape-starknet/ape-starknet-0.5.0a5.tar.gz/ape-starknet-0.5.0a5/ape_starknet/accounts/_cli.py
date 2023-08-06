from typing import List, cast

import click
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.cli import NetworkBoundCommand, ape_cli_context, existing_alias_argument, network_option
from ape.cli.options import ApeCliContextObject
from ape.logging import logger
from ape.utils import add_padding_to_strings

from ape_starknet.accounts import (
    BaseStarknetAccount,
    StarknetAccountContracts,
    StarknetKeyfileAccount,
)
from ape_starknet.utils import PLUGIN_NAME


def _get_container(cli_ctx: ApeCliContextObject) -> StarknetAccountContracts:
    return cast(StarknetAccountContracts, cli_ctx.account_manager.containers[PLUGIN_NAME])


@click.group("accounts")
def accounts():
    """Manage Starknet accounts"""


@accounts.command(cls=NetworkBoundCommand)
@ape_cli_context()
@click.argument("alias")
@network_option(ecosystem=PLUGIN_NAME)
@click.option("--token", help="Used for deploying contracts in Alpha Mainnet.")
@click.option(
    "--deployment-funder", help="Set as an alias to another Starknet account to fund and deploy."
)
def create(cli_ctx, alias, network, deployment_funder, token):
    """Create and/or deploy an account"""
    container = _get_container(cli_ctx)

    if alias in container.aliases:
        # Check if we have already deployed in this network.
        # The user will have to delete before they can deploy again.
        existing_account = container.load(alias)
        if existing_account.get_deployment(network):
            cli_ctx.abort(
                f"Account already deployed to '{network}' network. "
                f"Run 'ape starknet accounts delete <alias> --network {network}' "
                "first to re-deploy."
            )

    new_account = container.create_account(alias)
    cli_ctx.logger.success(f"Created account data for '{alias}'.")
    if not deployment_funder:
        return

    # Transfer money to new account
    is_local = cli_ctx.provider.network.name == LOCAL_NETWORK_NAME
    if is_local and not deployment_funder:
        # Helpful for demonstration purposes.
        deployment_funder = container.test_accounts[0]

    elif is_local and not deployment_funder.isnumeric():
        cli_ctx.abort("Use a numeric value (index) for a local devnet funder account.")

    elif is_local:
        funder_account = container.test_accounts[int(deployment_funder)]

    elif deployment_funder.startswith("0x"):
        # Load by address
        funder_account = container[deployment_funder]
    else:
        # Load by alias
        funder_account = container.load(deployment_funder)

    # Use the funder account to transfer an estimated cost of ETH to the new account
    # so it can be for its own deployment.

    txn = new_account.deploy_self_transaction
    txn = new_account.prepare_transaction(txn)
    funder_account.transfer(new_account, txn.max_fee)
    txn.signature = new_account.sign_transaction(txn)
    receipt = cli_ctx.provider.send_transaction(txn)
    contract_address_styled = click.style(receipt.contract_address, bold=True)
    logger.success(f"Account successfully deployed to '{contract_address_styled}'.")


@accounts.command(cls=NetworkBoundCommand)
@ape_cli_context()
@click.argument("alias")
@network_option(ecosystem=PLUGIN_NAME)
def deploy(cli_ctx, network, alias):
    """Deploy an existing, non-deployed account"""
    container = _get_container(cli_ctx)
    account = container.load(alias)
    account.deploy_self()
    contract_address = account.contract_address
    contract_address_styled = click.style(contract_address, bold=True)
    logger.success(f"Account successfully deployed to '{contract_address_styled}'.")


@accounts.command("list")
@ape_cli_context()
def _list(cli_ctx):
    """List your Starknet accounts"""

    starknet_accounts = [
        k
        for k in cast(List[StarknetKeyfileAccount], list(_get_container(cli_ctx).accounts))
        if isinstance(k, StarknetKeyfileAccount)
    ]

    if len(starknet_accounts) == 0:
        cli_ctx.logger.warning("No accounts found.")
        return

    num_accounts = len(starknet_accounts)
    header = f"Found {num_accounts} account"
    header += "s" if num_accounts > 1 else ""
    click.echo(f"{header}\n")

    for index in range(num_accounts):
        account = starknet_accounts[index]
        output_dict = {"Alias": account.alias, "Public key": account.public_key}
        for deployment in account.get_deployments():
            key = f"Contract address ({deployment.network_name})"
            output_dict[key] = deployment.contract_address

        output_keys = add_padding_to_strings(list(output_dict.keys()))
        output_dict = {k: output_dict[k.rstrip()] for k in output_keys}

        for k, v in output_dict.items():
            click.echo(f"{k} - {v}")

        if index < num_accounts - 1:
            click.echo()


@accounts.command(name="import")
@ape_cli_context()
@click.argument("alias")
@network_option(ecosystem=PLUGIN_NAME)
@click.option(
    "--address",
    help="The contract address of the account",
    callback=lambda ctx, param, value: ctx.obj.network_manager.starknet.decode_address(value)
    if value
    else None,
)
@click.option("--class-hash", help="The class hash of the account contract.")
@click.option("--salt", help="The contract address salt used when deploying the contract.")
def _import(cli_ctx, alias, network, address, class_hash, salt):
    """Add an existing account"""

    container = _get_container(cli_ctx)

    with cli_ctx.network_manager.parse_network_choice(network) as provider:
        network_name = provider.network.name

    if network_name == LOCAL_NETWORK_NAME:
        cli_ctx.abort("Must use --network option to specify non-local network.")

    if alias in container.aliases:
        existing_account = container.load(alias)

        if existing_account.get_deployment(network_name) or not isinstance(
            existing_account, StarknetKeyfileAccount
        ):
            cli_ctx.abort(f"Account already imported with '{network_name}' network.")

        click.echo(f"Importing existing account to network '{network_name}'.")
        existing_account.add_deployment(network_name, address)

    elif address:
        private_key = click.prompt("Enter private key", hide_input=True)
        container.import_account(
            alias, network_name, address, private_key, class_hash=class_hash, salt=salt
        )
    else:
        cli_ctx.abort("Please provide --address to import this account.")

    cli_ctx.logger.success(f"Import account '{alias}'.")


@accounts.command()
@ape_cli_context()
@existing_alias_argument(account_type=BaseStarknetAccount)
@network_option(ecosystem=PLUGIN_NAME)
def delete(cli_ctx, alias, network):
    """Delete an existing account"""
    container = _get_container(cli_ctx)

    if network == "starknet":
        # Did not specify a network and should use normally use default
        # However, if the account only exists on a single network, assume that one.
        account = container.load(alias)
        deployments = account.get_deployments()
        if len(deployments) == 1:
            network = deployments[0].network_name

    container.delete_account(alias, network=network)
    cli_ctx.logger.success(f"Account '{alias}' on network '{network}' has been deleted.")


@accounts.command()
@ape_cli_context()
@existing_alias_argument(account_type=StarknetKeyfileAccount)
def change_password(cli_ctx, alias):
    """Change the password of an existing account"""
    account = cli_ctx.account_manager.load(alias)
    account.change_password()
    cli_ctx.logger.success(f"Password has been changed for account '{alias}'")
