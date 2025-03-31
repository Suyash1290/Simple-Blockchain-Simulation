import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def tamper_block(self, index, new_transactions):
        if 0 < index < len(self.chain):
            self.chain[index].transactions = new_transactions
            self.chain[index].hash = self.chain[index].compute_hash()

    def display_chain(self):
        for block in self.chain:
            print(json.dumps({
                "index": block.index,
                "timestamp": block.timestamp,
                "transactions": block.transactions,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            }, indent=4))
            print("-" * 50)

if __name__ == "__main__":
    blockchain = Blockchain(difficulty=3)
    
    while True:
        print("1. Add Block")
        print("2. Display Blockchain")
        print("3. Check Validity")
        print("4. Tamper with Block")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            transactions = input("Enter transactions (comma separated): ").split(",")
            blockchain.add_block(transactions)
        elif choice == "2":
            blockchain.display_chain()
        elif choice == "3":
            print("Is blockchain valid?", blockchain.is_chain_valid())
        elif choice == "4":
            index = int(input("Enter block index to tamper: "))
            new_transactions = input("Enter new transactions (comma separated): ").split(",")
            blockchain.tamper_block(index, new_transactions)
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")
