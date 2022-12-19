# TornadoCash-Contract
- Tornado cash
- JavaScript


# how does it work ?

This function takes as parameters the web3 instance of the Web3 API, the origin address of the transaction, the destination address of the transaction and the value of the transaction in wei. It uses the Tornado Cash smart contract to generate a new anonymous address, then sends funds from the original address to the anonymous address. Then it uses the Tornado Cash smart contract to send funds from the anonymous address to the destination address.

Note that this function requires the installation of the Web3 API and knowledge of the TORNADO_CASH_ABI and TORNADO_CASH_ADDRESS values which are the application programming interface (ABI) and the smart contract address of Tornado Cash on Ethereum respectively. You can find these values on the Tornado Cash documentation page or by using a smart contract decryption service like Etherscan.
