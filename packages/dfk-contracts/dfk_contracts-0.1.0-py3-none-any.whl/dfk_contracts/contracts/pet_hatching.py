
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x576C260513204392F0eC0bc865450872025CB1cA",
    "sd": "0x22e656419Be8A0abf0B53D0941FfDC3B70Fea36e"
}

ABI = """[
    {"name": "EggCracked", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "eggId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "petId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "EggIncubated", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "eggId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "eggType", "type": "uint8", "indexed": true, "internalType": "uint8"}, {"name": "tier", "type": "uint8", "indexed": true, "internalType": "uint8"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "crack", "type": "function", "inputs": [{"name": "_eggId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "eggTypeCosts", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "eggAddress", "type": "address", "internalType": "address"}, {"name": "itemAddress1", "type": "address", "internalType": "address"}, {"name": "itemAmount1", "type": "uint16", "internalType": "uint16"}, {"name": "itemAddress2", "type": "address", "internalType": "address"}, {"name": "itemAmount2", "type": "uint16", "internalType": "uint16"}], "stateMutability": "view"},
    {"name": "getEgg", "type": "function", "inputs": [{"name": "_eggId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "petId", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "eggType", "type": "uint8", "internalType": "uint8"}, {"name": "seedblock", "type": "uint256", "internalType": "uint256"}, {"name": "finishTime", "type": "uint256", "internalType": "uint256"}, {"name": "tier", "type": "uint8", "internalType": "uint8"}], "internalType": "struct UnhatchedEgg"}], "stateMutability": "view"},
    {"name": "getUserEggs", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "incubateEgg", "type": "function", "inputs": [{"name": "_eggType", "type": "uint8", "internalType": "uint8"}, {"name": "_tier", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_petCoreAddress", "type": "address", "internalType": "address"}, {"name": "_jewelTokenAddress", "type": "address", "internalType": "address"}, {"name": "_goldAddress", "type": "address", "internalType": "address"}, {"name": "_gaiaTearsAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "jewelToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IJewelToken"}], "stateMutability": "view"},
    {"name": "originId", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "priceTiers", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "jewelCost", "type": "uint8", "internalType": "uint8"}, {"name": "goldCost", "type": "uint16", "internalType": "uint16"}, {"name": "tearCost", "type": "uint8", "internalType": "uint8"}, {"name": "incubationTime", "type": "uint32", "internalType": "uint32"}, {"name": "shinyChance", "type": "uint16", "internalType": "uint16"}], "stateMutability": "view"},
    {"name": "season", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "setAppearanceChoices", "type": "function", "inputs": [{"name": "_eggType", "type": "uint8", "internalType": "uint8"}, {"name": "_rarity", "type": "uint8", "internalType": "uint8"}, {"name": "_isSpecial", "type": "uint8", "internalType": "uint8"}, {"name": "_startIndex", "type": "uint256", "internalType": "uint256"}, {"name": "_endIndex", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setEggTypeCosts", "type": "function", "inputs": [{"name": "_eggType", "type": "uint8", "internalType": "uint8"}, {"name": "_eggTypeCost", "type": "tuple", "components": [{"name": "eggAddress", "type": "address", "internalType": "address"}, {"name": "itemAddress1", "type": "address", "internalType": "address"}, {"name": "itemAmount1", "type": "uint16", "internalType": "uint16"}, {"name": "itemAddress2", "type": "address", "internalType": "address"}, {"name": "itemAmount2", "type": "uint16", "internalType": "uint16"}], "internalType": "struct EggTypeCost"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setFees", "type": "function", "inputs": [{"name": "_feeAddresses", "type": "address[]", "internalType": "address[]"}, {"name": "_feePercents", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setOriginId", "type": "function", "inputs": [{"name": "_originId", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPetCore", "type": "function", "inputs": [{"name": "_petCoreAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPriceTiers", "type": "function", "inputs": [{"name": "_priceTierIndex", "type": "uint8", "internalType": "uint8"}, {"name": "_priceTier", "type": "tuple", "components": [{"name": "jewelCost", "type": "uint8", "internalType": "uint8"}, {"name": "goldCost", "type": "uint16", "internalType": "uint16"}, {"name": "tearCost", "type": "uint8", "internalType": "uint8"}, {"name": "incubationTime", "type": "uint32", "internalType": "uint32"}, {"name": "shinyChance", "type": "uint16", "internalType": "uint16"}], "internalType": "struct PriceTier"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "totalEggs", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class PetHatching(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def crack(self, cred:Credentials, _egg_id:uint256) -> TxReceipt:
        tx = self.contract.functions.crack(_egg_id)
        return self.send_transaction(tx, cred)

    def egg_type_costs(self, a:uint256) -> Tuple[address, address, uint16, address, uint16]:
        return self.contract.functions.eggTypeCosts(a).call()

    def get_egg(self, _egg_id:uint256) -> tuple:
        return self.contract.functions.getEgg(_egg_id).call()

    def get_user_eggs(self, _address:address) -> Sequence[uint256]:
        return self.contract.functions.getUserEggs(_address).call()

    def incubate_egg(self, cred:Credentials, _egg_type:uint8, _tier:uint8) -> TxReceipt:
        tx = self.contract.functions.incubateEgg(_egg_type, _tier)
        return self.send_transaction(tx, cred)

    def initialize(self, cred:Credentials, _pet_core_address:address, _jewel_token_address:address, _gold_address:address, _gaia_tears_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_pet_core_address, _jewel_token_address, _gold_address, _gaia_tears_address)
        return self.send_transaction(tx, cred)

    def jewel_token(self) -> address:
        return self.contract.functions.jewelToken().call()

    def origin_id(self) -> uint8:
        return self.contract.functions.originId().call()

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def price_tiers(self, a:uint256) -> Tuple[uint8, uint16, uint8, uint32, uint16]:
        return self.contract.functions.priceTiers(a).call()

    def season(self) -> uint8:
        return self.contract.functions.season().call()

    def set_appearance_choices(self, cred:Credentials, _egg_type:uint8, _rarity:uint8, _is_special:uint8, _start_index:uint256, _end_index:uint256) -> TxReceipt:
        tx = self.contract.functions.setAppearanceChoices(_egg_type, _rarity, _is_special, _start_index, _end_index)
        return self.send_transaction(tx, cred)

    def set_egg_type_costs(self, cred:Credentials, _egg_type:uint8, _egg_type_cost:tuple) -> TxReceipt:
        tx = self.contract.functions.setEggTypeCosts(_egg_type, _egg_type_cost)
        return self.send_transaction(tx, cred)

    def set_fees(self, cred:Credentials, _fee_addresses:Sequence[address], _fee_percents:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setFees(_fee_addresses, _fee_percents)
        return self.send_transaction(tx, cred)

    def set_origin_id(self, cred:Credentials, _origin_id:uint8) -> TxReceipt:
        tx = self.contract.functions.setOriginId(_origin_id)
        return self.send_transaction(tx, cred)

    def set_pet_core(self, cred:Credentials, _pet_core_address:address) -> TxReceipt:
        tx = self.contract.functions.setPetCore(_pet_core_address)
        return self.send_transaction(tx, cred)

    def set_price_tiers(self, cred:Credentials, _price_tier_index:uint8, _price_tier:tuple) -> TxReceipt:
        tx = self.contract.functions.setPriceTiers(_price_tier_index, _price_tier)
        return self.send_transaction(tx, cred)

    def total_eggs(self) -> uint256:
        return self.contract.functions.totalEggs().call()

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)