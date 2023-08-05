CONTRACT_RECEIVE_FUNCTION_SOURCE = """
pragma solidity ^0.6.0;


contract Receive {
    string text;

    fallback() external payable {
        text = 'fallback';
    }

    receive() external payable {
        text = 'receive';
    }

    function getText() public view returns (string memory) {
        return text;
    }

    function setText(string memory new_text) public returns (string memory) {
        return text = new_text;
    }
}
"""


CONTRACT_RECEIVE_FUNCTION_ABI = """
[
    {
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "inputs": [],
        "name": "getText",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "new_text",
                "type": "string"
            }
        ],
        "name": "setText",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    }
]
"""


CONTRACT_RECEIVE_FUNCTION_CODE = "608060405234801561001057600080fd5b506103da806100206000396000f3fe60806040526004361061002d5760003560e01c80635d3a1f9d14610092578063e00fe2eb146101ba57610063565b3661006357604080518082019091526007808252667265636569766560c81b60209092019182526100609160009161030c565b50005b6040805180820190915260088082526766616c6c6261636b60c01b60209092019182526100609160009161030c565b34801561009e57600080fd5b50610145600480360360208110156100b557600080fd5b8101906020810181356401000000008111156100d057600080fd5b8201836020820111156100e257600080fd5b8035906020019184600183028401116401000000008311171561010457600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295506101cf945050505050565b6040805160208082528351818301528351919283929083019185019080838360005b8381101561017f578181015183820152602001610167565b50505050905090810190601f1680156101ac5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156101c657600080fd5b50610145610275565b80516060906101e590600090602085019061030c565b805460408051602060026001851615610100026000190190941693909304601f810184900484028201840190925281815292918301828280156102695780601f1061023e57610100808354040283529160200191610269565b820191906000526020600020905b81548152906001019060200180831161024c57829003601f168201915b50505050509050919050565b60008054604080516020601f60026000196101006001881615020190951694909404938401819004810282018101909252828152606093909290918301828280156103015780601f106102d657610100808354040283529160200191610301565b820191906000526020600020905b8154815290600101906020018083116102e457829003601f168201915b505050505090505b90565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061034d57805160ff191683800117855561037a565b8280016001018555821561037a579182015b8281111561037a57825182559160200191906001019061035f565b5061038692915061038a565b5090565b61030991905b80821115610386576000815560010161039056fea2646970667358221220b93632f6dd6614e84675a1453e32b49de37a5d658a6e73173705c5a7dffc0bdd64736f6c63430006010033"  # noqa: E501


CONTRACT_RECEIVE_FUNCTION_RUNTIME = "60806040526004361061002d5760003560e01c80635d3a1f9d14610092578063e00fe2eb146101ba57610063565b3661006357604080518082019091526007808252667265636569766560c81b60209092019182526100609160009161030c565b50005b6040805180820190915260088082526766616c6c6261636b60c01b60209092019182526100609160009161030c565b34801561009e57600080fd5b50610145600480360360208110156100b557600080fd5b8101906020810181356401000000008111156100d057600080fd5b8201836020820111156100e257600080fd5b8035906020019184600183028401116401000000008311171561010457600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295506101cf945050505050565b6040805160208082528351818301528351919283929083019185019080838360005b8381101561017f578181015183820152602001610167565b50505050905090810190601f1680156101ac5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156101c657600080fd5b50610145610275565b80516060906101e590600090602085019061030c565b805460408051602060026001851615610100026000190190941693909304601f810184900484028201840190925281815292918301828280156102695780601f1061023e57610100808354040283529160200191610269565b820191906000526020600020905b81548152906001019060200180831161024c57829003601f168201915b50505050509050919050565b60008054604080516020601f60026000196101006001881615020190951694909404938401819004810282018101909252828152606093909290918301828280156103015780601f106102d657610100808354040283529160200191610301565b820191906000526020600020905b8154815290600101906020018083116102e457829003601f168201915b505050505090505b90565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061034d57805160ff191683800117855561037a565b8280016001018555821561037a579182015b8281111561037a57825182559160200191906001019061035f565b5061038692915061038a565b5090565b61030991905b80821115610386576000815560010161039056fea2646970667358221220b93632f6dd6614e84675a1453e32b49de37a5d658a6e73173705c5a7dffc0bdd64736f6c63430006010033"  # noqa: E501
