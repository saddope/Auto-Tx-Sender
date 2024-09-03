# AutoTxSender

AutoTxSender is a Python script that automates the sending of a high volume of Ethereum transactions. It is designed to help prepare wallets by generating transaction activity across various Ethereum-compatible networks. This can be useful for testing wallet functionality, building transaction history, or simulating network activity.

## Supported Networks

- **Arbitrum** (`arbitrum.py`)
- **Base** (`base.py`)
- **Optimism** (`optimism.py`)
- **Zora** (`zora.py`)

## Features

- Connects to Ethereum-compatible RPC networks.
- Sends transactions from a specified sender wallet to a receiver address.
- Supports multiple Ethereum-compatible networks for flexibility.
- Automatically retries on errors and waits between transactions.

## Installation

To get started, follow these steps:

1. **Ensure Python is Installed:**
   Make sure you have Python 3.11 or higher installed on your machine.

2. **Install Required Packages:**
   Use `pip` to install the necessary Python packages:

   ```bash
   pip install web3 eth-account

## Configuration

Before running the script, you need to configure it:

1. **Open `run.py`** in a text editor.

2. **Set the RPC URL:**
   Replace `YOUR_RPC_URL` with the URL of the Ethereum-compatible RPC network you want to use.

3. **Set the Private Key:**
   Replace `YOUR_PRIVATE_KEY` with your Ethereum wallet's private key.

4. **Set the Receiver Address:**
   Replace `0xRECEIVER_ADDRESS` with the recipient's Ethereum address.

## Usage

To run the script for a specific network, execute the corresponding file with the following command:

```bash
python arbitrum.py
```

```bash
python base.py
```

```bash
python optimism.py
```

```bash
python zora.py
```
Each script will continuously send transactions from the sender wallet to the specified receiver address. Adjust the settings in the script as needed to suit your use case.


## Notes

- **Security Warning:** Make sure to keep your private key secure. Do not share it or expose it in public repositories.
- **Network Fees:** Ensure you have enough ETH in your wallet to cover transaction fees.
- **Error Handling:** The script is designed to retry on errors and pause between transactions. Monitor the script's output for any issues.
