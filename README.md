![github-banner](https://user-images.githubusercontent.com/100821/108692834-6a115200-74fd-11eb-92df-ee07bf62b386.png)

# CLI client

## Installation

```
pip install lto-cli
```

[pip](https://pip.pypa.io/en/stable/) is the package installer for Python.

## Setup

### Manage accounts

```
lto accounts create
echo "my seed" | lto accounts seed --name foobar
lto accounts list
lto accounts set-default foobar
lto accounts remove 3JuijVBB7NCwCz2Ae5HhCDsqCXzeBLRTyeL
lto accounts show 3JuijVBB7NCwCz2Ae5HhCDsqCXzeBLRTyeL
```

### Public node

```
lto set-node https://nodes.lto.network
```

### Broadcast

Takes as input a transaction (signed or unsigned) and broadcast it to the network

```
echo $TX_JSON | lto broadcast
```
### Balance

Display the balances of the default address or if specified of a specific address
```
lto balance
```


## Transactions

### Anchor

```
lto anchor --hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

### Associations

```
lto association issue --recipient 3MyGpJh6Bb8auF3HtSr2dSJjqQVxgqLynpK --type 1 --hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
lto association revoke --recipient 3MyGpJh6Bb8auF3HtSr2dSJjqQVxgqLynpK --type 1 --hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

### Transfer

```
lto transfer --recipient 3MyGpJh6Bb8auF3HtSr2dSJjqQVxgqLynpK --amount 1000000000
```

### Mass-transfer

```
echo "3N6MFpSbbzTozDcfkTUT5zZ2sNbJKFyRtRj:1000000000
3NBC7ETcdPbf4QAXSop5UCJ53yX34aGPXoz:800000000" | lto mass-transfer
```

_Recipient/amount pairs are read from stdin._

### Leasing

```
lto lease create --recipient 3MyGpJh6Bb8auF3HtSr2dSJjqQVxgqLynpK --amount 1000000000
lto lease cancel --leaseid 6XmeG7SRWiw8pD6Uad6D9AAaY354v5TV6AJMhPpHMkqy
lto lease list
lto lease list-inbound
```

### Sponsorship

```
lto sponsorship create --recipient 3MyGpJh6Bb8auF3HtSr2dSJjqQVxgqLynpK
lto sponsorship cancel --recipient 3MyGpJh6Bb8auF3HtSr2dSJjqQVxgqLynpK
lto sponsorship list-inbound
```

## Common options

```
--network CHAINID
--account NAME|ADDRESS
--sponsor NAME|ADDRESS
--no-broadcast
--unsigned
```

#### `--network`

Use `--network T` to use testnet instead of mainnet. You need to setup accounts specifically for testnet.

#### `--account`

Select one of the accounts configured during setup. The account can be referenced by name or address. The name is only known locally.
If this option is omited, the default account is used.

#### `--sponsor`

Choose an account to sponsor the transaction. The sponsor will co-sign the transaction and pay the transaction fee.

_This feature is not yet available as it requires the Cobalt update to be activated._

#### `--no-broadcast`

Create and sign the transaction, but don't broadcast it to the node. The JSON will be outputted.

#### `--unsigned`

Create the transaction, but don't sign it. This option should only be used in combination with `--no-broadcast`.
