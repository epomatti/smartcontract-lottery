# Solidity Lottery

The does the app do:

1. Users can enter lottery with ETH based on a USD fee
2. An admin will choose when the lottery is over
3. The lottery will select a random winner using ChainLink oracle

How do we want to test this?

1. `mainnet-fork`
2. `development` with mocks
3. `testnet`

## Usage

```
sudo apt-get install python3-venv
python3 -m venv env
. env/bin/activate
pip install --upgrade pip
pip install eth-brownie
```

Need to remove `brownie` mainnet fork as we're using a custom fork.

```bash
brownie networks delete mainnet-fork
```

Add the mainnet fork:

```
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork='https://eth-mainnet.alchemyapi.io/v2/<YOUR KEY>' accounts=10 mnemonic=brownie port=8545
```
