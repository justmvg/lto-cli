import configparser
from LTO.AccountFactory import AccountFactory
from LTOCli import Config
from LTO.PublicNode import PublicNode

CHAIN_ID = 'L'
URL = 'https://nodes.lto.network'

def getSeedFromAddress(address):
    config = configparser.ConfigParser()
    config.read('L/accounts.ini')
    secName = Config.findAccountSection(address, config)
    if not secName:
        config.clear()
        config.read('T/accounts.ini')
        secName = Config.findAccountSection(address, config)
        if not secName:
            raise Exception ('No account found matching with default value')
        else:
            return config.get(secName, 'seed')
    else:
        return config.get(secName, 'seed')


def getAccount():
    global CHAIN_ID
    config = configparser.ConfigParser()
    config.read('L/config.ini')
    if 'Default' not in config.sections():
        raise Exception('No Default account set')
    address = config.get('Default', 'account')
    seed = getSeedFromAddress(address)
    if 'Node' in config.sections():
        CHAIN_ID = config.get('Node', 'chainId')
    account = AccountFactory(CHAIN_ID).createFromSeed(seed)
    return account

def getNode():
    global URL
    config = configparser.ConfigParser()
    config.read('L/config.ini')
    if 'Node' in config.sections():
        URL = config.get('Node', 'url')
    node = PublicNode(URL)
    return node

