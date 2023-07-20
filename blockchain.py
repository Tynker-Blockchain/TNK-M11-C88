import hashlib
import json
from time import time

def generateHash(input_string):
    hashObject = hashlib.sha256()
    hashObject.update(input_string.encode('utf-8'))
    hashValue = hashObject.hexdigest()
    return hashValue

class BlockChain():
    def __init__(self):
        self.chain = []

    def length(self):
        return len(self.chain)
        
    def addBlock(self, newBlock):
        if(len(self.chain) == 0):
            self.createGensisBlock()
        newBlock.previousHash = self.chain[-1].currentHash
        newBlock.currentHash = newBlock.calculateHash()
        self.chain.append(newBlock)
    
    def createGensisBlock(self):
        # Genesis block
        genesisBlock = Block(0, time(), {'sender':'NA', 'receiver':'NA', 'amount':'NA'}, "No Prevoius Hash Present. Since this is the first block.")
        self.chain.append(genesisBlock)
    
    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transaction", block.transaction)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print( "Is Valid Block",block.isValid)

            print("*" * 100 , "\n")

    # consensus protocol
    def validateBlock(self, currentBlock):
        # Getting previous block from block chain
        previousBlock = self.chain[currentBlock.index - 1]
       
        # Checking whether the current block index is greater than previous block index or not
        if(currentBlock.index != previousBlock.index + 1):
            return False
        
        # Gettting the previous block hash
        # previousBlockHash = previousBlock.calculateHash()

        # SA3
        # Modifiying the prevoius block timestamp attribute value by passing cureent timestamp
        previousBlockHash = previousBlock.calculateHash(time())


        # Checking whether the previous block hash and current block hash is equal or not 
        if(previousBlockHash != currentBlock.previousHash):
            return False
        
        return True
        

class Block:
    def __init__(self, index, timestamp, transaction, previousHash):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()
        self.isValid = None
       
    # SA3 : Set timestamp paramter as default None
    def calculateHash(self, timestamp=None):
        # Check when the timestamp is None the progam will use previous timestamp value
        if(timestamp == None):
            timestamp = self.timestamp

        blockString = str(self.index) + str(timestamp) + str(self.previousHash) + json.dumps(self.transaction)
        return generateHash(blockString)

   
    
    def showBlockDetails(self):
        print("Block Index", self.index)
        print("Timestamp", self.timestamp)
        print("Transaction", self.transaction)
        print( "Previous Hash",self.previousHash)
        print( "Current Hash",self.currentHash)
       

# transaction = {
#         'sender': 'Satoshi',
#         'receiver': 'Mike',
#         'amount': '5 ETH'
#     }

# sender = generateHash(transaction["sender"])
# receiver = generateHash(transaction["receiver"])

# transaction["sender"] = sender
# transaction["receiver"] = receiver

# blockData = {
#         'index': 1,
#         'timestamp': time(),
#         'transaction': transaction,
#         'previousHash': "No Prevoius Hash Present. Since this is the first block.",
#     }



# newBlock = Block(
#     blockData["index"], 
#     blockData["timestamp"], 
#     blockData["transaction"],
#     blockData["previousHash"])


# chain = BlockChain()
# chain.addBlock(newBlock)
# Validating the new block
#isValid = chain.validateBlock(newBlock)
# Changing isValid attribute value
#newBlock.isValid = isValid

# On Web SA3
#chain.printChain()



# SA1  : Write code for blockchain validation
# SA2  : Sandbox Activity
# SA3  : Validate the blockchain and if it is not valid block then show the message accordingly 