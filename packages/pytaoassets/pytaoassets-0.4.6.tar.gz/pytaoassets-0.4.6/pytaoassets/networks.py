from collections import namedtuple
from decimal import Decimal
from pytaoassets.exceptions import UnsupportedNetwork

# constants to be consumed by the backend
Constants = namedtuple('Constants', [
    'name',
    'shortname',
    'base58_prefixes',
    'base58_raw_prefixes',
    'bech32_hrp',
    'bech32_net',
    'xkeys_prefix',
    'xpub_version',
    'xprv_version',
    'wif_prefix',
    'from_unit',
    'to_unit',
    'min_tx_fee',
    'tx_timestamp',
    'op_return_max_bytes'
])


'''
Network name should be lowercase, for testnet append "-testnet".
For abbreviation prefix testnet of the network with "t".
'''

networks = (

    # Tao mainnet
    Constants(
        name='tao',
        shortname='xto',
        base58_prefixes={
            'T': 'p2pkh',
            '2': 'p2sh',
        },
        base58_raw_prefixes={
            'p2pkh': bytearray(b'\x42'),
            'p2sh': bytearray(b'\x03'),
        },
        bech32_hrp='tc',
        bech32_net='mainnet',
        xkeys_prefix='x',
        xpub_version=b'\x04\x88\xb2\x1e',
        xprv_version=b'\x04\x88\xad\xe4',
        wif_prefix=0x4c,
        from_unit=Decimal('1e-6'),
        to_unit=Decimal('1e6'),
        min_tx_fee=Decimal(0.0002),
        tx_timestamp=True,
        op_return_max_bytes=80
    ),

    Constants(
        name='peercoin',
        shortname='ppc',
        base58_prefixes={
            'P': 'p2pkh',
            'p': 'p2sh',
        },
        base58_raw_prefixes={
            'p2pkh': bytearray(b'\x37'),
            'p2sh': bytearray(b'\x75'),
        },
        bech32_hrp='bc',
        bech32_net='mainnet',
        xkeys_prefix='x',
        xpub_version=b'\x04\x88\xb2\x1e',
        xprv_version=b'\x04\x88\xad\xe4',
        wif_prefix=0xb7,
        from_unit=Decimal('1e-6'),
        to_unit=Decimal('1e6'),
        min_tx_fee=Decimal(0.01),
        tx_timestamp=True,
        op_return_max_bytes=80
    ),

    # Peercoin testnet
    Constants(
        name='peercoin-testnet',
        shortname='tppc',
        base58_prefixes={
            'm': 'p2pkh',
            'n': 'p2pkh',
        },
        base58_raw_prefixes={
            'p2pkh': bytearray(b'\x6f'),
            'p2sh': bytearray(b'\xc4'),
        },
        bech32_hrp='tb',
        bech32_net='testnet',
        xkeys_prefix='t',
        xpub_version=b'\x04\x35\x87\xcf',
        xprv_version=b'\x04\x35\x83\x94',
        wif_prefix=0xef,
        from_unit=Decimal('1e-6'),
        to_unit=Decimal('1e6'),
        min_tx_fee=Decimal(0.01),
        tx_timestamp=True,
        op_return_max_bytes=80
    )
)


def net_query(name: str) -> Constants:
    '''Find the NetworkParams for a network by its long or short name. Raises
    UnsupportedNetwork if no NetworkParams is found.
    '''

    for net_params in networks:
        if name in (net_params.name, net_params.shortname,):
            return net_params

    raise UnsupportedNetwork
