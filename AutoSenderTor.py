import time
from web3 import Web3

# Connectez-vous à un noeud Ethereum
web3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/YOUR_INFURA_API_KEY"))

# Récupérez le contrat Tornado Cash à partir de son adresse
tornado_cash_address = "0x3FDA67f7583380e67ef93072294a7Ac7E501D05f"
tornado_cash_contract = web3.eth.contract(address=tornado_cash_address, abi=TORNADO_CASH_ABI)

# Définissez l'adresse de retrait prédéfinie
withdrawal_address = "0xe81163b9eEbd9d2407F5Cc7f319339Db03065744"

# Générez un code de retrait en utilisant la fonction "createWithdrawal" du contrat Tornado Cash
def generate_withdrawal_code():
  withdrawal_code = tornado_cash_contract.functions.createWithdrawal(withdrawal_address, 100).call()
  return withdrawal_code

# Utilisez une boucle infinie pour exécuter le code de retrait de manière répétée
while True:
  withdrawal_code = generate_withdrawal_code()
  print("Withdrawal code generated: ", withdrawal_code)
  time.sleep(60) # Attendez 60 secondes avant de générer un nouveau code de retrait
