// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Notary { 



    uint public time;
    bytes32 public key;

    function init(bytes32 input) public{
        require(time==0);
        key=input;
        time=block.timestamp;

    }


}
