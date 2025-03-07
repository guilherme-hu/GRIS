from web3 import Web3

# Definições
RPC_URL = "	http://challs.grisufrj.com:48334/f4b7a768-1357-472d-9434-cab48176e3b1"
PRIVATE_KEY = "	0x6388b9b9f407c972ed1f98fca237315dd80289bc5ffaa660992c4cc8e5d77ca1"
CONTRACT_ADDRESS = "0x1eB263b6737F5d8b41b9414e8c821816ea41d48f"
WALLET_ADDRESS = "0x068cAF09371aF3bd4Db61b309792d39eaE6aafe6"

w3 = Web3(Web3.HTTPProvider(RPC_URL))
assert w3.is_connected(), "Erro: Falha na conexão com o RPC"


setup_abi = [{"inputs":[],"stateMutability":"payable","type":"constructor"},
             {"inputs":[],"name":"bb","outputs":[{"internalType":"contract BabyBlockchain","name":"","type":"address"}],"stateMutability":"view","type":"function"},
             {"inputs":[],"name":"isSolved","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]

setup_contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=setup_abi)

babyblockchain_addr = setup_contract.functions.bb().call()
print(f"Endereço da BabyBlockchain: {babyblockchain_addr}")

babyblockchain_abi = [{"inputs":[],"name":"solveChall","outputs":[],"stateMutability":"nonpayable","type":"function"},
                      {"inputs":[],"name":"solved","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]

babyblockchain_contract = w3.eth.contract(address=babyblockchain_addr, abi=babyblockchain_abi)

nonce = w3.eth.get_transaction_count(WALLET_ADDRESS)
tx = babyblockchain_contract.functions.solveChall().build_transaction({
    "from": WALLET_ADDRESS,
    "gas": 200000,
    "gasPrice": w3.to_wei("5", "gwei"),
    "nonce": nonce
})

signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
print(f"Transação enviada! Hash: {tx_hash.hex()}")

receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Transação confirmada no bloco {receipt.blockNumber}")

is_solved = babyblockchain_contract.functions.solved().call()
print(f"Desafio resolvido? {is_solved}")
