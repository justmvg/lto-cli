from lto.accounts.account_factory_ed25519 import AccountFactoryED25519 as AccountFactory
from lto_cli import config
import sys

def func(name_space, parser):
    if vars(name_space)['subparser-name-account'] == 'create':
        chain_id = name_space.network[0] if name_space.network else 'L'
        if not (chain_id.isalpha() and len(chain_id) == 1):
            parser.error('The --network parameter accepts only CHAR type')
        chain_id = chain_id.upper() if not chain_id.isupper() else chain_id
        sec_name = name_space.name[0] if name_space.name else ''
        factory = AccountFactory(chain_id)
        account = factory.create()
        config.write_to_file(chain_id, account, sec_name, parser)
        print(account.address)

    elif vars(name_space)['subparser-name-account'] == 'list':
        chain_id = name_space.network[0] if name_space.network else 'L'
        chain_id = chain_id.upper() if not chain_id.isupper() else chain_id
        config.print_list_accounts(chain_id, parser)



    elif vars(name_space)['subparser-name-account'] == 'set-default':
        config.set_default_accounts(name_space.address[0], parser)

    elif vars(name_space)['subparser-name-account'] == 'remove':
        config.remove_account(name_space.address[0], parser)

    elif vars(name_space)['subparser-name-account'] == 'show':
        config.show(name_space.address[0], parser)

    elif vars(name_space)['subparser-name-account'] == 'seed':
        chain_id = name_space.network[0] if name_space.network else 'L'
        if not (chain_id.isalpha() and len(chain_id) == 1):
            parser.error('The --network parameter accepts only CHAR type')
        chain_id = chain_id.upper() if not chain_id.isupper() else chain_id
        sec_name = name_space.name[0] if name_space.name else ''
        factory = AccountFactory(chain_id)
        seed = name_space.stdin.read().splitlines()
        if not seed:
            parser.error("Seed missing, type 'lto account seed --help' for instructions")
        account = factory.create_from_seed(seed[0])
        config.write_to_file(chain_id, account, sec_name, parser)

    else:
        parser.error('Type lto account --help for instructions')
