from typing import TYPE_CHECKING, Dict, Union, cast

from ape.api import AccountAPI, Address
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.contracts import ContractInstance
from ape.exceptions import ContractError
from ape.types import AddressType
from ape.utils import cached_property
from eth_typing import HexAddress, HexStr
from ethpm_types import ContractType
from starknet_devnet.fee_token import FeeToken
from starknet_py.constants import FEE_CONTRACT_ADDRESS

from ape_starknet.exceptions import ContractTypeNotFoundError, StarknetProviderError
from ape_starknet.utils.basemodel import StarknetBase

if TYPE_CHECKING:
    from ape_starknet.accounts import BaseStarknetAccount


def missing_contract_error(token: str, contract_address: AddressType) -> ContractError:
    return ContractError(f"Incorrect '{token}' contract address '{contract_address}'.")


ERC20 = ContractType(
    **{
        "contractName": "ERC20",
        "abi": [
            {
                "type": "struct",
                "name": "Uint256",
                "members": [
                    {"name": "low", "type": "felt", "offset": 0},
                    {"name": "high", "type": "felt", "offset": 1},
                ],
                "size": 2,
            },
            {
                "type": "event",
                "name": "Transfer",
                "inputs": [
                    {"name": "from_", "type": "felt", "indexed": False},
                    {"name": "to", "type": "felt", "indexed": False},
                    {"name": "value", "type": "Uint256", "indexed": False},
                ],
                "anonymous": False,
            },
            {
                "type": "event",
                "name": "Approval",
                "inputs": [
                    {"name": "owner", "type": "felt", "indexed": False},
                    {"name": "spender", "type": "felt", "indexed": False},
                    {"name": "value", "type": "Uint256", "indexed": False},
                ],
                "anonymous": False,
            },
            {
                "type": "constructor",
                "stateMutability": "nonpayable",
                "inputs": [
                    {"name": "name", "type": "felt"},
                    {"name": "symbol", "type": "felt"},
                    {"name": "decimals", "type": "felt"},
                    {"name": "initial_supply", "type": "Uint256"},
                    {"name": "recipient", "type": "felt"},
                ],
            },
            {
                "type": "function",
                "name": "name",
                "stateMutability": "view",
                "inputs": [],
                "outputs": [{"name": "name", "type": "felt"}],
            },
            {
                "type": "function",
                "name": "symbol",
                "stateMutability": "view",
                "inputs": [],
                "outputs": [{"name": "symbol", "type": "felt"}],
            },
            {
                "type": "function",
                "name": "totalSupply",
                "stateMutability": "view",
                "inputs": [],
                "outputs": [{"name": "totalSupply", "type": "Uint256"}],
            },
            {
                "type": "function",
                "name": "decimals",
                "stateMutability": "view",
                "inputs": [],
                "outputs": [{"name": "decimals", "type": "felt"}],
            },
            {
                "type": "function",
                "name": "balanceOf",
                "stateMutability": "view",
                "inputs": [{"name": "account", "type": "felt"}],
                "outputs": [{"name": "balance", "type": "Uint256"}],
            },
            {
                "type": "function",
                "name": "allowance",
                "stateMutability": "view",
                "inputs": [{"name": "owner", "type": "felt"}, {"name": "spender", "type": "felt"}],
                "outputs": [{"name": "remaining", "type": "Uint256"}],
            },
            {
                "type": "function",
                "name": "transfer",
                "stateMutability": "nonpayable",
                "inputs": [
                    {"name": "recipient", "type": "felt"},
                    {"name": "amount", "type": "Uint256"},
                ],
                "outputs": [{"name": "success", "type": "felt"}],
            },
            {
                "type": "function",
                "name": "transferFrom",
                "stateMutability": "nonpayable",
                "inputs": [
                    {"name": "sender", "type": "felt"},
                    {"name": "recipient", "type": "felt"},
                    {"name": "amount", "type": "Uint256"},
                ],
                "outputs": [{"name": "success", "type": "felt"}],
            },
            {
                "type": "function",
                "name": "approve",
                "stateMutability": "nonpayable",
                "inputs": [
                    {"name": "spender", "type": "felt"},
                    {"name": "amount", "type": "Uint256"},
                ],
                "outputs": [{"name": "success", "type": "felt"}],
            },
            {
                "type": "function",
                "name": "increaseAllowance",
                "stateMutability": "nonpayable",
                "inputs": [
                    {"name": "spender", "type": "felt"},
                    {"name": "added_value", "type": "Uint256"},
                ],
                "outputs": [{"name": "success", "type": "felt"}],
            },
            {
                "type": "function",
                "name": "decreaseAllowance",
                "stateMutability": "nonpayable",
                "inputs": [
                    {"name": "spender", "type": "felt"},
                    {"name": "subtracted_value", "type": "Uint256"},
                ],
                "outputs": [{"name": "success", "type": "felt"}],
            },
        ],
    }
)
TEST_TOKEN_ADDRESS = "0x07394cbe418daa16e42b87ba67372d4ab4a5df0b05c6e554d158458ce245bc10"


class TokenManager(StarknetBase):
    # The 'test_token' refers to the token that comes with Argent-X
    additional_tokens: Dict = {}
    contract_type = ERC20
    local_balance_cache: Dict[AddressType, Dict[str, int]] = {}

    @property
    def token_address_map(self) -> Dict:
        return {
            **self._base_token_address_map,
            **self.additional_tokens,
        }

    @cached_property
    def _base_token_address_map(self):
        local_eth = self.starknet.decode_address(FeeToken.ADDRESS)
        live_eth = self.starknet.decode_address(FEE_CONTRACT_ADDRESS)
        live_token = self.starknet.decode_address(TEST_TOKEN_ADDRESS)

        if self.provider.network.name == LOCAL_NETWORK_NAME:
            self.chain_manager.contracts[local_eth] = self.contract_type
        else:
            self.chain_manager.contracts[live_eth] = self.contract_type

        return {
            "eth": {"local": local_eth, "mainnet": live_eth, "testnet": live_eth},
            "test_token": {"testnet": live_token, "mainnet": live_token},
        }

    def __getitem__(self, token: str) -> ContractInstance:
        network = self.provider.network.name
        contract_address = AddressType(
            HexAddress(HexStr(self.token_address_map[token.lower()].get(network)))
        )
        if not contract_address:
            raise ContractTypeNotFoundError(contract_address)

        return ContractInstance(contract_address, ERC20)

    def is_token(self, address: AddressType) -> bool:
        network = self.provider.network.name
        return any(address == networks.get(network) for networks in self.token_address_map.values())

    def add_token(self, name: str, network: str, address: AddressType):
        if name not in self.additional_tokens:
            self.additional_tokens[name] = {}

        self.additional_tokens[name][network] = address

    def get_balance(self, account: Union[Address, AddressType], token: str = "eth") -> int:
        if hasattr(account, "address"):
            address = cast(Address, account).address
        else:
            address = cast(AddressType, account)

        if self.provider.network.name != LOCAL_NETWORK_NAME:
            return self._get_balance(address, token=token)

        if address not in self.local_balance_cache:
            balance = self._get_balance(address, token=token)
            self.local_balance_cache[address] = {token: balance}

        elif token not in self.local_balance_cache[address]:
            self.local_balance_cache[address][token] = self._get_balance(address, token=token)

        return self.local_balance_cache[address][token]

    def _get_balance(self, account: AddressType, token: str = "eth") -> int:
        account_int = int(account, 16)
        result = self[token].balanceOf(account_int)
        if isinstance(result, (tuple, list)):
            if len(result) == 2:
                low, high = result
                return (high << 128) + low

            return result[0]

        return result

    def transfer(
        self,
        sender: Union[int, AddressType, "BaseStarknetAccount"],
        receiver: Union[int, AddressType, "BaseStarknetAccount"],
        amount: int,
        token: str = "eth",
    ):
        if isinstance(receiver, int):
            receiver_address = self.starknet.decode_address(receiver)
            receiver_address_int = receiver
        elif hasattr(receiver, "address_int"):
            receiver_address_int = receiver.address_int  # type: ignore
            receiver_address = receiver.address  # type: ignore
        elif isinstance(receiver, str):
            receiver_address_int = self.starknet.encode_address(receiver)
            receiver_address = self.starknet.decode_address(receiver)
        else:
            raise StarknetProviderError(
                f"Unhandled type for receiver '{receiver}'. Expects int, str, or account."
            )

        sender_account = (
            self.account_contracts[sender] if isinstance(sender, (int, str)) else sender
        )
        result = self[token].transfer(receiver_address_int, amount, sender=sender_account)
        if self.provider.network.name != LOCAL_NETWORK_NAME:
            return result

        # NOTE: the fees paid by the sender get updated in `provider.send_transaction()`.
        amount_int = self._convert_amount_to_int(amount)
        self.update_cache(sender_account.address, -amount_int, token=token)
        self.update_cache(receiver_address, amount_int, token=token)
        return result

    def update_cache(
        self, address: Union[AccountAPI, AddressType], amount: Union[int, Dict], token: str = "eth"
    ):
        amount_int = self._convert_amount_to_int(amount)
        address_str: str
        if isinstance(address, AccountAPI):
            address_str = address.address
        else:
            address_str = address

        if address_str not in self.local_balance_cache:
            self.local_balance_cache[address_str] = {
                token: self._get_balance(address_str, token=token)
            }

            # Return, as this should include what we were updating to.
            return

        elif token not in self.local_balance_cache[address_str]:
            self.local_balance_cache[address_str][token] = self._get_balance(
                address_str, token=token
            )

            # Return, as this should include what we were updating to.
            return

        current_balance: int = self.local_balance_cache[address_str][token]
        if current_balance + amount_int < 0:
            raise ValueError(
                "Unable to set balance to negative value. "
                f"Current balance={current_balance}, amount={amount_int}"
            )

        self.local_balance_cache[address_str][token] += amount_int

    def _convert_amount_to_int(self, amount: Union[int, Dict]) -> int:
        if isinstance(amount, int):
            return amount

        elif isinstance(amount, dict) and amount.get("high", 0):
            return (amount["high"] << 128) + amount["low"]

        elif isinstance(amount, dict):
            return amount["low"]

        else:
            raise TypeError(f"Unknown amount type: '{amount}'")
