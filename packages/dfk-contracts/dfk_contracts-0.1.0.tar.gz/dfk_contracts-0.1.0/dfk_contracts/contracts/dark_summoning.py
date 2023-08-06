
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x70908Fd7278aab183C7EfC4f3449184E98e2e305",
    "sd": ""
}

ABI = """[
    {"name": "CrystalAirdrop", "type": "event", "inputs": [{"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "crystalId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "CrystalDarkSummoned", "type": "event", "inputs": [{"name": "crystalId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "summonerId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "assistantId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "generation", "type": "uint16", "internalType": "uint16", "indexed": false}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "enhancementStone", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "CrystalOpen", "type": "event", "inputs": [{"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "crystalId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "heroId", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "CrystalSummoned", "type": "event", "inputs": [{"name": "crystalId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "summonerId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "assistantId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "generation", "type": "uint16", "internalType": "uint16", "indexed": false}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "enhancementStone", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "EnhancementStoneAdded", "type": "event", "inputs": [{"name": "atunementItemAddress", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "internalType": "uint8", "indexed": false}], "anonymous": false},
    {"name": "activeEnhancementStones", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "addEnhancementStone", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "baseCooldown", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "baseSummonFee", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "calculateRarityBonusCost", "type": "function", "inputs": [{"name": "_rarityBonusCharges", "type": "uint8", "internalType": "uint8"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
    {"name": "calculateSummoningCost", "type": "function", "inputs": [{"name": "_hero", "type": "tuple", "internalType": "struct Hero", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "internalType": "struct SummoningInfo", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}]}, {"name": "info", "type": "tuple", "internalType": "struct HeroInfo", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}]}, {"name": "state", "type": "tuple", "internalType": "struct HeroState", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum HeroStatus"}]}, {"name": "stats", "type": "tuple", "internalType": "struct HeroStats", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}]}, {"name": "primaryStatGrowth", "type": "tuple", "internalType": "struct HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "secondaryStatGrowth", "type": "tuple", "internalType": "struct HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "professions", "type": "tuple", "internalType": "struct HeroProfessions", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}]}]}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "cooldownPerGen", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "feeAddresses", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "feePercents", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "increasePerGen", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "increasePerSummon", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "powerToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IPowerToken"}], "stateMutability": "view"},
    {"name": "removeEnhancementStone", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTears", "type": "function", "inputs": [{"name": "_tearsAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "summonCrystal", "type": "function", "inputs": [{"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_summonerTears", "type": "uint16", "internalType": "uint16"}, {"name": "_assistantTears", "type": "uint16", "internalType": "uint16"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}, {"name": "_rarityBonusCharges", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class DarkSummoning(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def active_enhancement_stones(self, a:address) -> bool:
        return self.contract.functions.activeEnhancementStones(a).call()

    def add_enhancement_stone(self, cred:Credentials, _address:address) -> TxReceipt:
        tx = self.contract.functions.addEnhancementStone(_address)
        return self.send_transaction(tx, cred)

    def base_cooldown(self) -> uint256:
        return self.contract.functions.baseCooldown().call()

    def base_summon_fee(self) -> uint256:
        return self.contract.functions.baseSummonFee().call()

    def calculate_rarity_bonus_cost(self, _rarity_bonus_charges:uint8) -> uint256:
        return self.contract.functions.calculateRarityBonusCost(_rarity_bonus_charges).call()

    def calculate_summoning_cost(self, _hero:tuple) -> uint256:
        return self.contract.functions.calculateSummoningCost(_hero).call()

    def cooldown_per_gen(self) -> uint256:
        return self.contract.functions.cooldownPerGen().call()

    def fee_addresses(self, a:uint256) -> address:
        return self.contract.functions.feeAddresses(a).call()

    def fee_percents(self, a:uint256) -> uint256:
        return self.contract.functions.feePercents(a).call()

    def increase_per_gen(self) -> uint256:
        return self.contract.functions.increasePerGen().call()

    def increase_per_summon(self) -> uint256:
        return self.contract.functions.increasePerSummon().call()

    def power_token(self) -> address:
        return self.contract.functions.powerToken().call()

    def remove_enhancement_stone(self, cred:Credentials, _address:address) -> TxReceipt:
        tx = self.contract.functions.removeEnhancementStone(_address)
        return self.send_transaction(tx, cred)

    def set_tears(self, cred:Credentials, _tears_address:address) -> TxReceipt:
        tx = self.contract.functions.setTears(_tears_address)
        return self.send_transaction(tx, cred)

    def summon_crystal(self, cred:Credentials, _summoner_id:uint256, _assistant_id:uint256, _summoner_tears:uint16, _assistant_tears:uint16, _enhancement_stone:address, _rarity_bonus_charges:uint8) -> TxReceipt:
        tx = self.contract.functions.summonCrystal(_summoner_id, _assistant_id, _summoner_tears, _assistant_tears, _enhancement_stone, _rarity_bonus_charges)
        return self.send_transaction(tx, cred)