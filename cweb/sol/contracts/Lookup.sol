// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Lookup { 



    mapping (bytes32 => address payable) public register;

    function def(bytes32 where,address payable what) public {
        require(available(where),"This Name is already defined");
        register[where]=what;
    }
    function available(bytes32 where) public view returns (bool) {
        return register[where]==address(0);
    }


}
