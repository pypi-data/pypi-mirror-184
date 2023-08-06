import random

import pytest

from ape_starknet.utils import get_random_private_key

from .conftest import ApeStarknetCliRunner


@pytest.fixture(scope="module")
def accounts_runner(ape_cli):
    return ApeStarknetCliRunner(ape_cli, ["starknet", "accounts"])


@pytest.fixture(scope="module")
def root_accounts_runner(ape_cli):
    return ApeStarknetCliRunner(ape_cli, ["accounts"])


def test_create_then_deploy(accounts_runner, account_container):
    random_alias = "".join(random.choice(["a", "b", "c", "d", "e", "f"]) for _ in range(6))
    output = accounts_runner.invoke("create", random_alias)
    assert "Creating account data for" in output

    # Fund the account so it can deploy
    account = account_container.load(random_alias)
    funder = account_container.test_accounts[5]
    funder.transfer(account, "1 ETH")

    output = accounts_runner.invoke("deploy", random_alias)
    assert "Account successfully deployed to " in output


def test_create_and_depoy(accounts_runner):
    random_alias = "".join(random.choice(["a", "b", "c", "d", "e", "f"]) for _ in range(6))
    output = accounts_runner.invoke("create", random_alias, "--deployment-funder", "5")
    assert "Creating account data for" in output
    assert "Account successfully deployed to " in output


def test_delete(
    accounts_runner, key_file_account, password, existing_key_file_alias, contract_address
):
    """
    This integration test deletes a single deployment of an account and then
    re-import it. The account never completely goes away because it is deployed on
    multiple networks.
    """
    output = accounts_runner.invoke(
        "delete",
        existing_key_file_alias,
        "--network",
        "starknet:testnet",
        input=password,
    )
    assert existing_key_file_alias in output
    output = accounts_runner.invoke("list")

    # The account should still have a remaining deployment and thus still found in output
    assert existing_key_file_alias in output

    # Only the testnet deployment should have gotten deleted
    output_lines = output.split("\n")
    for index in range(len(output_lines)):
        line = output_lines[index]
        if existing_key_file_alias not in line:
            continue

        # Find the deployments parts
        next_index = index + 1
        for next_line in output_lines[next_index:]:
            if not next_line.strip():
                break  # Reached end of account's section

            if next_line.startswith("Contract address (testnet)"):
                assert contract_address not in next_line, "Deployment failed to delete"

    # Re-import the deployment (clean-up)
    accounts_runner.invoke(
        "import",
        existing_key_file_alias,
        "--network",
        "starknet:testnet",
        "--address",
        contract_address,
        input=password,
    )


@pytest.mark.parametrize(
    "private_key",
    (
        get_random_private_key(),
        "0x0097a6a4998e2eb47d4cea623c9f8b3048764fc38a92616bdf1c3e68be8b5e28",
        267944034277627769235577208827196223019601239705086925741947749358138777128,
    ),
)
def test_import(
    accounts_runner,
    key_file_account,
    account_container,
    private_key,
    existing_key_file_alias,
    password,
):
    network = "starknet:testnet"  # NOTE: Does not actually connect
    account_path = account_container.data_folder / f"{existing_key_file_alias}.json"
    address = key_file_account.address

    if account_path.is_file():
        # Corrupted from previous test
        account_path.unlink()

    accounts_runner.invoke(
        "import",
        existing_key_file_alias,
        "--network",
        network,
        "--address",
        address,
        input=[private_key, password, password],
    )

    # Clean-up
    accounts_runner.invoke(
        "delete",
        existing_key_file_alias,
        "--network",
        network,
        input=[password, "y"],
    )


def test_import_when_local(accounts_runner):
    output = accounts_runner.invoke(
        "import",
        "FAILS",
        "--address",
        "0x0098580e36aB1485C66f0DC95C2c923e734B7Af44D04dD2B5b9d0809Aa672033",
        ensure_successful=False,
    )
    assert "ERROR: Must use --network option to specify non-local network." in output


def test_list(
    accounts_runner, key_file_account, existing_key_file_alias, public_key, contract_address
):
    output = accounts_runner.invoke("list")
    assert existing_key_file_alias in output
    assert contract_address in output
    assert public_key in output


def test_core_accounts_list_all(root_accounts_runner, key_file_account, existing_key_file_alias):
    # This is making sure the normal `ape accounts list --all` command works.
    assert existing_key_file_alias in root_accounts_runner.invoke("list", "--all")


def test_change_password(accounts_runner, key_file_account, password, existing_key_file_alias):
    new_password = "321"
    assert "SUCCESS" in accounts_runner.invoke(
        "change-password", existing_key_file_alias, input=[password, new_password, new_password]
    )
    assert "SUCCESS" in accounts_runner.invoke(
        "change-password", existing_key_file_alias, input=[new_password, password, password]
    )
