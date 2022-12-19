# TornadoCash-Contract
- Tornado cash
- JavaScript


# how does it work ? Contract

This function takes as parameters the web3 instance of the Web3 API, the origin address of the transaction, the destination address of the transaction and the value of the transaction in wei. It uses the Tornado Cash smart contract to generate a new anonymous address, then sends funds from the original address to the anonymous address. Then it uses the Tornado Cash smart contract to send funds from the anonymous address to the destination address.

Note that this function requires the installation of the Web3 API and knowledge of the TORNADO_CASH_ABI and TORNADO_CASH_ADDRESS values which are the application programming interface (ABI) and the smart contract address of Tornado Cash on Ethereum respectively. You can find these values on the Tornado Cash documentation page or by using a smart contract decryption service like Etherscan.

# how does it work ? the tornado cash generator and verify and code autosender

Make sure you have installed the necessary dependencies, such as Node.js and npm (Node.js package manager).

Create a new Node.js project using the npm init command.

Install the necessary libraries for your project, like web3.js (a JavaScript library to interact with the Ethereum blockchain) and @Tornado-Cash/vault (a JavaScript library to interact with Tornado Cash). You can install them using the command 'npm install --save web3 @tornado-cash/vault
