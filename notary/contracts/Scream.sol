// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Scream { 

    event doo(address indexed from,uint value);

    function run(uint what) public {
        emit doo (msg.sender,what);
    }




}
