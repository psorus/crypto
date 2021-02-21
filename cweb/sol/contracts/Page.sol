// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Page { 



    address payable public owner;
    bytes public content;

    function update(bytes calldata text) public {
        require(msg.sender==owner,"Only the owner can change the content of this page");
        content=text;
    }
    function tip() payable public {
        require(msg.value>0,"Tipping usually involves money");

    }
    function payout() public returns (uint){
        require(msg.sender==owner);
        uint amount=address(this).balance;
        owner.transfer(amount);
        return amount;
    }
    constructor() { owner = payable(msg.sender); }


}
