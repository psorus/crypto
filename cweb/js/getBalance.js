

load("require.js");
load("await.js");

/*
A simple script that defines an address, gets the balance of it and then converts it to Ether before showing the result in the console.
For an explanation of this code, navigate to the wiki https://github.com/ThatOtherZach/Web3-by-Example/wiki/Get-Balance
*/

// Require the web3 node module.
//var Web3 = require('web3');

let Web3= await require(['web3']);
print(Web3);


// Show Web3 where it needs to look for a connection to Ethereum.
web3 = new Web3(new Web3.providers.HttpProvider('https://kovan.infura.io/v3/c83277c8952e4e1280aa1a853fb18fcf'));

// Write to the console the script will run shortly.
print('Getting Ethereum address info.....');

// Define the address to search witin.
var addr = ("0x33b0cd164decc76a20cf9080e06c52e5cd7a030e");

// Show the address in the console.
print('Address:', addr);

// Use Wb3 to get the balance of the address, convert it and then show it in the console.
web3.eth.getBalance(addr, function (error, result) {
	if (!error)
		console.log('Ether:', web3.utils.fromWei(result,'ether')); // Show the ether balance after converting it from Wei
	else
		console.log('Huston we have a promblem: ', error); // Should dump errors here
});
