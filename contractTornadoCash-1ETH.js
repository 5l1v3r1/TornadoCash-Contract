const Web3 = require('web3');

async function sendAnonymousTransaction(web3, from, to, value) {

  const tornadoCashContract = new web3.eth.Contract(TORNADO_CASH_ABI, TORNADO_CASH_ADDRESS);


  const anonymousAddress = await tornadoCashContract.methods.deposit().call({ from: from });


  await web3.eth.sendTransaction({ from: from, to: anonymousAddress, value: value });


  await tornadoCashContract.methods.send(to, value).send({ from: anonymousAddress });
}


const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_API_KEY'));
const from = '0x0000000000000000000000000000000000000000';
const to = '0xe81163b9eEbd9d2407F5Cc7f319339Db03065744';
const value = '1000000000000000000'; // 1 ETH en wei
sendAnonymousTransaction(web3, from, to, value);
