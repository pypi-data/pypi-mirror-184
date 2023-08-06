import functools
import json
from dataclasses import dataclass
from math import ceil
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Union

import click
from ape.api import AccountAPI, AccountContainerAPI, ReceiptAPI, TransactionAPI
from ape.api.address import BaseAddress
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.exceptions import (
    AccountsError,
    APINotImplementedError,
    ProviderNotConnectedError,
    SignatureError,
)
from ape.logging import LogLevel, logger
from ape.types import AddressType, TransactionSignature
from ape.utils import cached_property
from eth_keyfile import create_keyfile_json, decode_keyfile_json
from eth_utils import add_0x_prefix, text_if_str, to_bytes
from ethpm_types import ContractType
from hexbytes import HexBytes
from pydantic import Field, validator
from starknet_py.net import KeyPair
from starknet_py.net.signer.stark_curve_signer import StarkCurveSigner
from starknet_py.utils.crypto.facade import ECSignature, message_signature, pedersen_hash
from starkware.cairo.lang.vm.cairo_runner import verify_ecdsa_sig
from starkware.starknet.core.os.class_hash import compute_class_hash
from starkware.starknet.core.os.contract_address.contract_address import (
    calculate_contract_address_from_hash,
)
from starkware.starknet.definitions.fields import ContractAddressSalt
from starkware.starknet.services.api.contract_class import ContractClass

from ape_starknet.exceptions import ContractTypeNotFoundError, StarknetProviderError
from ape_starknet.provider import StarknetProvider
from ape_starknet.transactions import (
    AccountTransaction,
    DeployAccountTransaction,
    InvokeFunctionTransaction,
)
from ape_starknet.types import StarknetSignableMessage
from ape_starknet.utils import (
    OPEN_ZEPPELIN_ACCOUNT_CLASS_HASH,
    OPEN_ZEPPELIN_ACCOUNT_CONTRACT_TYPE,
    get_chain_id,
    get_random_private_key,
    pad_hex_str,
    to_checksum_address,
)
from ape_starknet.utils.basemodel import StarknetBase

APP_KEY_FILE_KEY = "ape-starknet"
"""
The key-file stanza containing custom properties
specific to the ape-starknet plugin.
"""
APP_KEY_FILE_VERSION = "0.1.0"

# https://github.com/starkware-libs/cairo-lang/blob/v0.9.1/src/starkware/starknet/cli/starknet_cli.py#L66
FEE_MARGIN_OF_ESTIMATION = 1.1


def sign_calldata(calldata: Iterable[int], priv_key: int):
    """
    Helper function that signs hash:

        hash = pedersen_hash(calldata[0], 0)
        hash = pedersen_hash(calldata[1], hash)
        hash = pedersen_hash(calldata[2], hash)
        ...

    :param calldata: iterable of ints
    :param priv_key: private key
    :return: signed calldata's hash
    """
    hashed_calldata = functools.reduce(lambda x, y: pedersen_hash(y, x), calldata, 0)
    return message_signature(hashed_calldata, priv_key)


class StarknetAccountContracts(AccountContainerAPI, StarknetBase):

    ephemeral_accounts: Dict[str, Dict] = {}
    """Local-network accounts that do not persist."""

    cached_accounts: Dict[str, "StarknetKeyfileAccount"] = {}
    """Accounts created in a live network that persist in key-files."""

    @property
    def provider_config(self) -> Dict:
        return self.starknet_config["provider"]

    @property
    def number_of_devnet_accounts(self) -> int:
        if not self.network_manager.active_provider:
            return 0

        if self.provider.network.name != LOCAL_NETWORK_NAME:
            return 0

        return self.provider_config.local["number_of_accounts"]  # type: ignore

    @property
    def devnet_account_seed(self) -> int:
        return self.provider_config.local["seed"]  # type: ignore

    @property
    def _key_file_paths(self) -> Iterator[Path]:
        for path in self.data_folder.glob("*.json"):
            if path.stem not in ("deployments_map",):
                yield path

    @property
    def aliases(self) -> Iterator[str]:
        yield from self.ephemeral_accounts.keys()
        for key_file in self._key_file_paths:
            yield key_file.stem

    @property
    def public_key_addresses(self) -> Iterator[AddressType]:
        for account in self.accounts:
            yield account.address

    @property
    def test_accounts(self) -> List["StarknetDevelopmentAccount"]:
        if (
            self.network_manager.active_provider is None
            or self.provider.network.name != LOCAL_NETWORK_NAME
            or not isinstance(self.provider, StarknetProvider)
        ):
            return []

        return self._test_accounts

    @cached_property
    def _test_accounts(self):
        try:
            predeployed_accounts = self.provider.devnet_client.predeployed_accounts
        except ProviderNotConnectedError:
            logger.warning("Devnet not running")
            return []

        devnet_accounts = [
            StarknetDevelopmentAccount.parse_obj(acc) for acc in predeployed_accounts
        ]

        # Track all devnet account contracts in chain manager for look-up purposes
        for account in devnet_accounts:
            self.chain_manager.contracts[account.address] = account.contract_type

        return devnet_accounts

    @property
    def accounts(self) -> Iterator[AccountAPI]:
        for test_account in self.test_accounts:
            yield test_account

        for alias, account_data in self.ephemeral_accounts.items():
            yield StarknetDevelopmentAccount.parse_obj(account_data)

        for key_file_path in self._key_file_paths:
            if key_file_path.stem == "deployments_map":
                continue

            if key_file_path.stem in self.cached_accounts:
                yield self.cached_accounts[key_file_path.stem]
            else:
                account = StarknetKeyfileAccount(key_file_path=key_file_path)
                self.cached_accounts[key_file_path.stem] = account
                yield account

    def __len__(self) -> int:
        return len([*self._key_file_paths])

    def __setitem__(self, address: AddressType, account: AccountAPI):
        pass

    def __delitem__(self, address: AddressType):
        pass

    def __getitem__(self, item: Union[AddressType, int]) -> AccountAPI:
        address_int = item if isinstance(item, int) else int(item, 16)

        # First, check if user accessing via public key
        for account in [a for a in self.accounts if isinstance(a, BaseStarknetAccount)]:
            if int(account.public_key, 16) == address_int:
                return super().__getitem__(account.address)

        # Else, use the contract address (more expected)
        checksum_address = self.starknet.decode_address(address_int)
        return super().__getitem__(checksum_address)

    def get_account(self, address: Union[AddressType, int]) -> "BaseStarknetAccount":
        return self[address]  # type: ignore

    def load(self, alias: str) -> "BaseStarknetAccount":
        if alias in self.ephemeral_accounts:
            return StarknetDevelopmentAccount.parse_obj(self.ephemeral_accounts[alias])

        return self.load_key_file_account(alias)

    def load_key_file_account(self, alias: str) -> "StarknetKeyfileAccount":
        if alias in self.cached_accounts:
            return self.cached_accounts[alias]

        for key_file_path in self._key_file_paths:
            if key_file_path.stem == alias:
                account = StarknetKeyfileAccount(key_file_path=key_file_path)
                self.cached_accounts[alias] = account
                return account

        raise AccountsError(f"Starknet account '{alias}' not found.")

    def create_account(
        self,
        alias: str,
        class_hash: int = OPEN_ZEPPELIN_ACCOUNT_CLASS_HASH,
        salt: Optional[int] = None,
        private_key: Optional[str] = None,
    ) -> "BaseStarknetAccount":
        if alias in self.aliases:
            raise AccountsError(f"Account with alias '{alias}' already exists.")

        network_name = self.provider.network.name
        private_key = private_key or get_random_private_key()
        key_pair = KeyPair.from_private_key(int(private_key, 16))
        salt = salt or ContractAddressSalt.get_random_value()
        contract_address = calculate_contract_address_from_hash(
            salt,
            class_hash,
            [key_pair.public_key],
            0,
        )
        address_str = to_checksum_address(contract_address)
        logger.info(f"Creating account data for '{address_str}' ...")
        return self.import_account(
            alias, network_name, contract_address, private_key, class_hash=class_hash, salt=salt
        )

    def import_account(
        self,
        alias: str,
        network_name: str,
        contract_address: str,
        private_key: Union[int, str],
        passphrase: Optional[str] = None,
        class_hash: int = OPEN_ZEPPELIN_ACCOUNT_CLASS_HASH,
        salt: Optional[int] = None,
    ) -> "BaseStarknetAccount":
        address = self.starknet.decode_address(contract_address)
        if isinstance(private_key, str) and private_key.startswith("0x"):
            private_key = pad_hex_str(private_key.strip("'\""))
            private_key = int(private_key, 16)
        elif isinstance(private_key, str):
            private_key = int(private_key)

        network_name = _clean_network_name(network_name)
        key_pair = KeyPair.from_private_key(private_key)
        deployments = [{"network_name": network_name, "contract_address": address}]
        new_account: "BaseStarknetAccount"

        if network_name == LOCAL_NETWORK_NAME:
            account_data = {
                "public_key": key_pair.public_key,
                "private_key": key_pair.private_key,
                "address": contract_address,
                "salt": salt or 20,
                "class_hash": class_hash,
            }
            self.ephemeral_accounts[alias] = account_data
            new_account = StarknetDevelopmentAccount.parse_obj(account_data)
        else:
            # Only write keyfile if not in a local network
            path = self.data_folder.joinpath(f"{alias}.json")
            new_account = StarknetKeyfileAccount(key_file_path=path)
            new_account.write(
                passphrase=passphrase,
                private_key=private_key,
                class_hash=class_hash,
                deployments=deployments,
            )

        # Ensure contract gets cached
        network = self.starknet.get_network(network_name)
        with network.use_provider(network.default_provider or "starknet"):
            contract_type = self.starknet_explorer.get_contract_type(address)
            if not contract_type:
                ContractTypeNotFoundError(address)

            if contract_type:
                self.chain_manager.contracts[address] = contract_type

        return new_account

    def delete_account(
        self, alias: str, network: Optional[str] = None, passphrase: Optional[str] = None
    ):
        network = _clean_network_name(network) if network else self.provider.network.name
        if alias in self.ephemeral_accounts:
            del self.ephemeral_accounts[alias]
        else:
            account = self.load_key_file_account(alias)
            account.delete(network, passphrase=passphrase)


@dataclass
class StarknetAccountDeployment:
    network_name: str
    contract_address: AddressType


class BaseStarknetAccount(AccountAPI, StarknetBase):
    contract_type: ContractType = OPEN_ZEPPELIN_ACCOUNT_CONTRACT_TYPE
    salt: Optional[int] = None

    @property
    def signer(self) -> StarkCurveSigner:
        raise APINotImplementedError("Implement 'signer' in base class.")

    @cached_property
    def class_hash(self) -> int:
        bytecode_obj = self.contract_type.deployment_bytecode
        if not bytecode_obj or not bytecode_obj.bytecode:
            raise ValueError("Missing ContractClass bytes")

        contract_cls = ContractClass.deserialize(HexBytes(bytecode_obj.bytecode))
        return compute_class_hash(contract_cls)

    @property
    def public_key(self) -> str:
        raise APINotImplementedError("Implement `public_key` in a base class.")

    @property
    def address_int(self) -> int:
        return self.starknet.encode_address(self.address)

    @cached_property
    def deploy_self_transaction(self) -> DeployAccountTransaction:
        self.salt = self.salt or ContractAddressSalt.get_random_value()
        return DeployAccountTransaction(
            salt=self.salt,
            class_hash=self.class_hash,
            constructor_calldata=[int(self.public_key, 16)],
        )

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.address}>"

    def call(self, txn: TransactionAPI, send_everything: bool = False) -> ReceiptAPI:
        if send_everything:
            raise NotImplementedError("send_everything currently isn't implemented in Starknet.")

        elif not isinstance(txn, AccountTransaction):
            raise AccountsError("Can only call Starknet account transactions.")

        txn = self.prepare_transaction(txn)
        if not txn.signature:
            raise SignatureError("The transaction was not signed.")

        return self.provider.send_transaction(txn)

    def deploy_self(self) -> ReceiptAPI:
        """
        Deploys this account.

        Returns:
            :class:`~ape.api.transactions.ReceiptAPI`: The receipt from the
            :class:`~ape_starknet.transactions.DeployAccountTransaction`.
        """
        return self.call(self.deploy_self_transaction)

    def prepare_transaction(self, txn: TransactionAPI) -> TransactionAPI:
        if not isinstance(txn, AccountTransaction):
            return txn

        txn = self._prepare_transaction(txn)
        if not txn.max_fee:
            # NOTE: Signature cannot be None when estimating fees.
            txn.signature = self.sign_transaction(txn)
            txn.max_fee = ceil(self.get_fee_estimate(txn) * FEE_MARGIN_OF_ESTIMATION)

        txn.signature = self.sign_transaction(txn)
        return txn

    def _prepare_transaction(self, txn: TransactionAPI) -> TransactionAPI:
        if isinstance(txn, AccountTransaction):
            # Set now to prevent infinite loop
            txn.is_prepared = True

        txn = super().prepare_transaction(txn)
        if isinstance(txn, InvokeFunctionTransaction):
            return txn.as_execute()

        return txn

    def get_fee_estimate(self, txn: TransactionAPI) -> int:
        return self.provider.estimate_gas_cost(txn)

    def sign_transaction(self, txn: TransactionAPI) -> TransactionSignature:
        if not isinstance(txn, AccountTransaction):
            raise AccountsError(
                f"This account can only sign Starknet transactions (received={type(txn)}."
            )

        # NOTE: 'v' is not used
        stark_txn = txn.as_starknet_object()
        sign_result = self.signer.sign_transaction(stark_txn)
        if not sign_result:
            raise SignatureError("Failed to sign transaction.")

        r = to_bytes(sign_result[0])
        s = to_bytes(sign_result[1])
        return TransactionSignature(v=0, r=r, s=s)  # type: ignore

    def transfer(
        self,
        account: Union[str, AddressType, BaseAddress],
        value: Union[str, int, None] = None,
        data: Union[bytes, str, None] = None,
        **kwargs,
    ) -> ReceiptAPI:
        value = value or 0
        value = self.conversion_manager.convert(value, int) or 0
        if not isinstance(value, int):
            if value.isnumeric():
                value = str(value)
            else:
                raise StarknetProviderError("value is not an integer.")

        if not isinstance(account, str) and hasattr(account, "address"):
            receiver = getattr(account, "address")

        elif isinstance(account, str):
            checksummed_address = self.starknet.decode_address(account)
            receiver = self.starknet.encode_address(checksummed_address)

        elif isinstance(account, int):
            receiver = account

        else:
            raise TypeError(f"Unable to handle account type '{type(account)}'.")

        return self.tokens.transfer(self.address, receiver, value, **kwargs)

    def check_signature(  # type: ignore
        self,
        data: int,
        signature: Optional[ECSignature] = None,  # TransactionAPI doesn't need it
    ) -> bool:
        public_key_int = self.starknet.encode_address(self.public_key)
        return verify_ecdsa_sig(public_key_int, data, signature)

    def declare(self, contract_type: ContractType):
        txn = self.starknet.encode_contract_blueprint(contract_type, sender=self.address)
        return self.call(txn)

    def _create_signer(self, private_key: int) -> StarkCurveSigner:
        key_pair = KeyPair.from_private_key(private_key)
        return StarkCurveSigner(
            account_address=self.address,
            key_pair=key_pair,
            chain_id=get_chain_id(self.provider.chain_id),
        )


class StarknetDevelopmentAccount(BaseStarknetAccount):
    contract_address: AddressType = Field(alias="address")
    """
    The contract address of the account.
    Either where it is deployed to or where it is going to be deployed to.
    """

    private_key: str
    """
    The account's private key.
    """

    salt: int = 20
    """
    The contract-address salt used when deploying this account.
    Defaults to ``20`` because it's the same value ``starknet_devnet`` uses.
    """

    # Alias because base-class needs `public_key` as a @property
    pub_key: str = Field(alias="public_key")
    """
    The public key of the account. Aliased from ``public_key`` because that is
    a ``@property`` in the base class.
    """

    @validator("contract_address", "pub_key", "private_key", pre=True, allow_reuse=True)
    def validate_int_to_hex(cls, value):
        return to_checksum_address(value)

    @property
    def public_key(self) -> str:
        return self.pub_key

    @cached_property
    def public_key_int(self) -> int:
        return int(self.public_key, 16)

    @cached_property
    def address(self) -> AddressType:
        return self.contract_address

    @cached_property
    def signer(self) -> StarkCurveSigner:
        return self._create_signer(int(self.private_key, 16))

    def sign_message(  # type: ignore[override]
        self, msg: StarknetSignableMessage
    ) -> Optional[ECSignature]:
        msg = StarknetSignableMessage(value=msg)
        return sign_calldata(msg.value, int(self.private_key, 16))


class StarknetKeyfileAccount(BaseStarknetAccount):
    key_file_path: Path
    locked: bool = True
    __autosign: bool = False
    __cached_key: Optional[int] = None

    @cached_property
    def signer(self) -> StarkCurveSigner:
        return self._create_signer(self.__get_private_key())

    @property
    def address(self) -> AddressType:
        for deployment in self.get_deployments():
            network_name = deployment.network_name
            network = self.starknet.networks[network_name]
            if network_name == network.name:
                contract_address = deployment.contract_address
                return self.starknet.decode_address(contract_address)

        raise AccountsError("Account not deployed.")

    @property
    def alias(self) -> Optional[str]:
        return self.key_file_path.stem

    @cached_property
    def class_hash(self) -> int:
        return self.get_account_data().get("class_hash") or OPEN_ZEPPELIN_ACCOUNT_CLASS_HASH

    @property
    def public_key(self) -> str:
        account_data = self.get_account_data()
        if "address" not in account_data:
            raise StarknetProviderError(
                f"Account data corrupted, missing 'address' key: {account_data}."
            )

        address = account_data["address"]
        if isinstance(address, int):
            address = HexBytes(address).hex()

        return add_0x_prefix(address)

    def prepare_transaction(self, txn: TransactionAPI) -> TransactionAPI:
        txn = self._prepare_transaction(txn)
        do_relock = False
        if not txn.max_fee:
            if self.locked:
                # Unlock to prevent multiple prompts for signing transaction.
                original_level = logger.level
                logger.set_level(LogLevel.ERROR)
                self.set_autosign(True)
                logger.set_level(original_level)

            txn.signature = self.sign_transaction(txn)
            txn.max_fee = ceil(self.get_fee_estimate(txn) * FEE_MARGIN_OF_ESTIMATION)

        txn.signature = self.sign_transaction(txn)

        if do_relock:
            self.locked = True
            self.set_autosign(False)

        return txn

    def get_account_contract_type(self) -> ContractType:
        return OPEN_ZEPPELIN_ACCOUNT_CONTRACT_TYPE

    def write(
        self,
        passphrase: Optional[str] = None,
        private_key: Optional[int] = None,
        class_hash: int = OPEN_ZEPPELIN_ACCOUNT_CLASS_HASH,
        deployments: Optional[List[Dict]] = None,
    ):
        passphrase = (
            click.prompt("Enter a new passphrase", hide_input=True, confirmation_prompt=True)
            if passphrase is None
            else passphrase
        )
        key_file_data = self.__encrypt_key_file(passphrase, private_key=private_key)
        account_data = self.get_account_data()
        if deployments:
            if APP_KEY_FILE_KEY not in account_data:
                account_data[APP_KEY_FILE_KEY] = {}

            account_data[APP_KEY_FILE_KEY]["deployments"] = deployments

        account_data = {**account_data, **key_file_data, "class_hash": class_hash}
        self.key_file_path.write_text(json.dumps(account_data))

    def get_account_data(self) -> Dict:
        if self.key_file_path.is_file():
            return json.loads(self.key_file_path.read_text())

        return {}

    def delete(self, network: str, passphrase: Optional[str] = None):
        passphrase = (
            click.prompt(
                f"Enter passphrase to delete '{self.alias}'",
                hide_input=True,
            )
            if passphrase is None
            else passphrase
        )

        try:
            self.__decrypt_key_file(passphrase)
        except FileNotFoundError:
            return

        network = _clean_network_name(network)
        deployments = self.get_deployments()
        if network not in [d.network_name for d in deployments]:
            raise AccountsError(f"Account '{self.alias}' not deployed to network '{network}'.")

        remaining_deployments = [
            vars(d) for d in self.get_deployments() if d.network_name != network
        ]
        if remaining_deployments:
            self.write(passphrase=passphrase, deployments=remaining_deployments)
        elif click.confirm(f"Completely delete local key for account '{self.address}'?"):
            # Delete entire account JSON if no more deployments.
            # The user has to agree to an additional prompt since this may be very destructive.
            self.key_file_path.unlink()

    def sign_message(  # type: ignore[override]
        self, msg: StarknetSignableMessage, passphrase: Optional[str] = None
    ) -> Optional[ECSignature]:
        msg = StarknetSignableMessage(value=msg)
        private_key = self.__get_private_key(passphrase=passphrase)
        return sign_calldata(msg.value, private_key)

    def change_password(self):
        self.locked = True  # force entering passphrase to get key
        original_passphrase = self._get_passphrase_from_prompt()
        private_key = self.__get_private_key(passphrase=original_passphrase)
        self.write(passphrase=None, private_key=private_key)

    def add_deployment(self, network_name: str, contract_address: AddressType):
        passphrase = self._get_passphrase_from_prompt()
        network_name = _clean_network_name(network_name)
        deployments = [
            vars(d) for d in self.get_deployments() if d.network_name not in network_name
        ]
        new_deployment = StarknetAccountDeployment(
            network_name=network_name, contract_address=contract_address
        )
        deployments.append(vars(new_deployment))

        self.write(
            passphrase=passphrase,
            private_key=self.__get_private_key(passphrase=passphrase),
            deployments=deployments,
        )

    def unlock(self, passphrase: Optional[str] = None):
        passphrase = passphrase or self._get_passphrase_from_prompt(
            f"Enter passphrase to unlock '{self.alias}'"
        )
        self.__get_private_key(passphrase=passphrase)
        self.locked = False

    def set_autosign(self, enabled: bool, passphrase: Optional[str] = None):
        if enabled:
            self.unlock(passphrase=passphrase)
            logger.warning("Danger! This account will now sign any transaction its given.")

        self.__autosign = enabled
        if not enabled:
            # Re-lock if was turning off
            self.locked = True
            self.__cached_key = None

    def get_deployments(self) -> List[StarknetAccountDeployment]:
        plugin_key_file_data = self.get_account_data().get(APP_KEY_FILE_KEY, {})
        return [StarknetAccountDeployment(**d) for d in plugin_key_file_data.get("deployments", [])]

    def get_deployment(self, network_name: str) -> Optional[StarknetAccountDeployment]:
        # NOTE: d is not None check only because mypy is confused
        return next(
            filter(
                lambda d: d is not None and d.network_name in network_name, self.get_deployments()
            ),
            None,
        )

    def __get_private_key(self, passphrase: Optional[str] = None) -> int:
        if self.__cached_key is not None:
            if not self.locked:
                click.echo(f"Using cached key for '{self.alias}'")
                return self.__cached_key
            else:
                self.__cached_key = None

        if passphrase is None:
            passphrase = self._get_passphrase_from_prompt()

        key_hex_str = self.__decrypt_key_file(passphrase).hex()
        key = int(key_hex_str, 16)
        if self.locked and (
            passphrase is not None or click.confirm(f"Leave '{self.alias}' unlocked?")
        ):
            self.locked = False
            self.__cached_key = key

        return key

    def _get_passphrase_from_prompt(self, message: Optional[str] = None) -> str:
        message = message or f"Enter passphrase to unlock '{self.alias}'"
        return click.prompt(
            message,
            hide_input=True,
            default="",  # Just in case there's no passphrase
        )

    def __encrypt_key_file(self, passphrase: str, private_key: Optional[int] = None) -> Dict:
        private_key = (
            self.__get_private_key(passphrase=passphrase) if private_key is None else private_key
        )
        key_str = pad_hex_str(HexBytes(private_key).hex())
        passphrase_bytes = text_if_str(to_bytes, passphrase)
        return create_keyfile_json(HexBytes(key_str), passphrase_bytes, kdf="scrypt")

    def __decrypt_key_file(self, passphrase: str) -> HexBytes:
        key_file_dict = json.loads(self.key_file_path.read_text())
        password_bytes = text_if_str(to_bytes, passphrase)
        decoded_json = decode_keyfile_json(key_file_dict, password_bytes)
        return HexBytes(decoded_json)


def _clean_network_name(network: str) -> str:
    for net in ("local", "mainnet", "testnet"):
        if net in network:
            return net

    if "goerli" in network:
        return "testnet"

    return network


def _create_key_file_app_data(deployments: List[Dict[str, str]]) -> Dict:
    return {APP_KEY_FILE_KEY: {"version": APP_KEY_FILE_VERSION, "deployments": deployments}}


__all__ = [
    "StarknetAccountContracts",
    "StarknetKeyfileAccount",
]
