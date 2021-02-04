// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract MLB { //MultiLockedBox


    mapping(address => bytes32) internal locks;
    address[] public holder;
    address public creator;

    event keylogger(address _who,bytes32 _what);
    
    constructor(){creator=msg.sender;}

    function is_holder(address who) public view returns (bool){
        for(uint i=0;i<holder.length;++i){
            if(holder[i]==who){return true;}
        }
        return false;
    }
    function has_key_for(address who) public view returns (bool){
        if(!is_holder(who)){return false;}
        return locks[who]!=0;
    }
    function add_holder(address who) public returns (bool){
        require(msg.sender==creator,"You are not allowed to do this");
        if(is_holder(who)){return false;}
        holder.push(who);
        return true;
    }

    function openlock(bytes32 lock) public returns (bool){
        require(is_holder(msg.sender),"You dont own a lock");
        if(has_key_for(msg.sender)){return false;}
        locks[msg.sender]=lock;
        emit keylogger(msg.sender,lock);
        return true;
    }
    
    function lock_count() public view returns (uint){
        return holder.length;
    }

    function missing_locks() public view returns (int){
        int ret=0;
        for(uint i=0;i<holder.length;++i){
            if(!has_key_for(holder[i])){++ret;}
        }
        return ret;
    }
    /*function get_all_locks() public view returns (bytes32[] memory){
        int constant lc=lock_count();
        bytes32[lc] ret;
        for(int i=0;i<holder.length;++i){
            if(!has_key_for(holder[i])){ret[i]=locks[holder[i]];}
        }
        return ret;
    }*/


}
