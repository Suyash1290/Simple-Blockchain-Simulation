# Simple Blockchain Simulation

## Overview
This project is a simple blockchain simulation written in Python. It mimics core blockchain functionalities such as block creation, proof-of-work mining, chain validation, and tamper detection.

## Features
- **Block Structure**: Each block contains an index, timestamp, transactions, previous block hash, and its own hash.
- **Mining with Proof-of-Work**: Blocks are mined using a simple proof-of-work mechanism.
- **Blockchain Management**: Ability to add blocks, display the chain, validate integrity, and simulate tampering.
- **User Input Support**: Users can add transactions, tamper with blocks, and check blockchain validity via an interactive menu.

## Requirements
Ensure you have Python installed (Python 3.x recommended).

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_link>
   cd <repository_directory>
   ```
2. Install dependencies (if any):
   ```sh
   pip install -r requirements.txt  # (Not required for basic functionality)
   ```

## Usage
Run the script using:
```sh
python blockchain.py
```

### Menu Options:
1. **Add Block**: Enter transactions to be added to a new block.
2. **Display Blockchain**: View the details of all blocks in the chain.
3. **Check Validity**: Verify if the blockchain is valid.
4. **Tamper with Block**: Modify an existing block’s transactions to see how the blockchain detects tampering.
5. **Exit**: Quit the program.

## Example Output
```
1. Add Block
2. Display Blockchain
3. Check Validity
4. Tamper with Block
5. Exit
Enter your choice: 1
Enter transactions (comma separated): Alice->Bob:10, Bob->Charlie:5

Block added successfully!
```

## Tampering Demonstration
If you modify a block's data, the blockchain validation will fail, indicating tampering.

## License
This project is open-source and available under the MIT License.

## Author
Suyash Verma

