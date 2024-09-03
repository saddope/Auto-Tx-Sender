from web3 import Web3
from eth_account import Account
import time

# Connect to the RPC network (replace with your own RPC URL)
rpc_url = 'YOUR_RPC_URL_HERE'
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Check connection
if not web3.is_connected():
    print("Failed to connect to the network")
    exit()

# Sender's private key and receiver's address (replace with your own values)
sender_private_key = 'YOUR_PRIVATE_KEY_HERE'
receiver_address = 'YOUR_RECEIVER_ADDRESS_HERE'

# Determine the sender's address
try:
    sender_address = Account.from_key(sender_private_key).address
except Exception as e:
    print(f"Error generating sender address: {e}")
    exit()

# Function to send a transaction
def send_transaction(sender_private_key, receiver_address):
    # Get nonce
    nonce = web3.eth.get_transaction_count(sender_address)

    # Transaction parameters
    transaction = {
        'nonce': nonce,
        'to': receiver_address,
        'value': web3.to_wei(0, 'ether'),  # Send 0 ETH
        'gas': 65852,  # Gas limit
        'maxFeePerGas': web3.to_wei(0.02, 'gwei'),  # Maximum gas price
        'maxPriorityFeePerGas': web3.to_wei(0.00000001, 'gwei'),  # Priority gas fee
        'chainId': 42161  # Chain ID for Arbitrum
    }

    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(transaction, sender_private_key)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    # Wait for transaction confirmation
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    
    print(f"Transaction sent: {web3.to_hex(tx_hash)}")
    return tx_receipt

# Main loop for sending transactions
def main():
    while True:
        try:
            receipt = send_transaction(sender_private_key, receiver_address)
            print(f"Transaction confirmed: {receipt.transactionHash.hex()}")
            time.sleep(1)  # Wait between transactions (1 second)
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()
