from web3 import Web3
from eth_account import Account
import time

# Connect to the Zora RPC network (replace with your own RPC URL)
zora_rpc_url = 'YOUR_ZORA_RPC_URL_HERE'  # Replace with your Zora RPC URL
web3 = Web3(Web3.HTTPProvider(zora_rpc_url))

# Check connection
if not web3.is_connected():
    print("Failed to connect to the Zora network")
    exit()

# Sender's private key and receiver's address (replace with your own values)
sender_private_key = 'YOUR_PRIVATE_KEY_HERE'  # Replace with your sender's private key
receiver_address = 'RECEIVER_ADDRESS_HERE'  # Replace with the receiver's address

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
        'gas': 21000,  # Gas limit
        'gasPrice': web3.to_wei(0.003010751, 'gwei')  # Gas price
    }

    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(transaction, sender_private_key)

    # Send the transaction
    try:
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transaction sent: {web3.to_hex(tx_hash)}")
        return tx_hash
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None

# Main loop for sending transactions
def main():
    while True:
        try:
            tx_hash = send_transaction(sender_private_key, receiver_address)
            if tx_hash:
                tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
                print(f"Transaction confirmed: {tx_receipt.transactionHash.hex()}")
            else:
                print("Transaction was not sent.")
            time.sleep(1)  # Delay of 1 second between transactions
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()
