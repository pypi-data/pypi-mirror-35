import pytest
from os import urandom
from decimal import Decimal
import time
from pytaoassets.kutil import Kutil
from pytaoassets.provider import Explorer
from pytaoassets.networks import net_query
from pytaoassets.transactions import tx_output, find_parent_outputs, p2pkh_script
from taopy.structs.transaction import PeercoinMutableTx, PeercoinTx, Locktime
from taopy.structs.sig import P2pkhSolver


def test_key_generation():
    '''test privkey/pubkey generation.'''

    mykey = Kutil(network="xto")

    assert isinstance(mykey.privkey, str)
    assert isinstance(mykey.pubkey, str)


def test_key_generation_from_seed():
    '''check if key generation is what is expected from seed.'''

    seed = "Hello PeerAssets."
    mykey = Kutil(from_string=seed, network="xto")

    assert mykey.privkey == '680510f7f5e622347bc8d9e54e109a9192353693ef61d82d2d5bdf4bc9fd638b'
    assert mykey.pubkey == '037cf9e7664b5d10ce209cf9e2c7f68baa06f1950114f25677531b959edd7e670c'


def test_address_generation():
    '''test if addresses are properly made'''

    privkey = bytearray(urandom(32))

    assert Kutil(network="xto", privkey=privkey).address.startswith("P")

    assert isinstance(Kutil(network='xto').address, str)
    assert len(Kutil(network='xto').address) == 34


def test_mainnet_wif_import():
    '''test importing WIF privkey'''

    mykey = Kutil(network='xto', from_wif="CHTwXavkWCVi5PVFUDmCvRiJPZpzo1imLC9FEG4u4LakbnU7TU7f")

    assert mykey.address == 'TbdCceyr7sTxTKydxtDTPwoFhdDwY8T3Tv'
    assert mykey.pubkey == '0374113EA30D602A111DAFBECF0F7F5B72E139D257BB8ED7CC0E458E9594892C47'
    assert mykey.privkey == '4784326D5470603F569CF9BA257B7BAFD2A5D296AC61CEC44576FE7AD5EE0C7E'


def test_wif_export():
    '''test Kutil WIF export'''

    mykey = Kutil(network='xto',
                  privkey=bytearray.fromhex('1b19749afd007bf6db0029e0273a46409bc160b9349031752bbc3cd913bbbdd3')
                 )

    assert isinstance(mykey.wif, str)
    assert mykey.wif == 'CHTwXavkWCVi5PVFUDmCvRiJPZpzo1imLC9FEG4u4LakbnU7TU7f'


def test_sign_transaction():

    network_params = net_query('xto')
    provider = Explorer(network='xto')
    key = Kutil(network='xto',
                privkey=bytearray.fromhex('4784326D5470603F569CF9BA257B7BAFD2A5D296AC61CEC44576FE7AD5EE0C7E')
                )
    dest_address = 'mwn75Gavp6Y1tJxca53HeCj5zzERqWagr6'

    unspent = provider.select_inputs(key.address, 0.63)  # 0.69
    output = tx_output(network='xto',
                       value=Decimal(0.1),
                       n=0, script=p2pkh_script(network='xto',
                                                address=dest_address)
                       )

    unsigned = TaoMutableTx(version=1,
                                 timestamp=int(time.time()),
                                 ins=unspent['utxos'],
                                 outs=[output],
                                 network=network_params,
                                 locktime=Locktime(0)
                                 )

    parent_outputs = [find_parent_outputs(provider, i) for i in unsigned.ins]
    solver = P2pkhSolver(key._private_key)

    signed = unsigned.spend(parent_outputs,
                            [solver for i in parent_outputs])

    assert isinstance(signed, PeercoinTx)
