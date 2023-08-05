

import pytest
import time
from decimal import Decimal

from taopy.structs.transaction import (
    Locktime,
    TxOut,
    MutableTransaction,
    PeercoinMutableTx,
    Transaction
)

from taopy.structs.script import P2pkhScript

from pytaoassets.transactions import (
    calculate_tx_fee,
    make_raw_transaction,
    p2pkh_script,
    tx_output,
    sign_transaction
)

from pytaoassets.networks import net_query
import pytaoassets as pa


@pytest.mark.parametrize("tx_size", [181, 311])
def test_calculate_transaction_fee(tx_size):

    assert round(calculate_tx_fee(tx_size), 2) == round(Decimal(0.01), 2)


@pytest.mark.parametrize("network", ['tao'])
def test_tx_output(network):

    if network == 'tao':
        addr = 'TbdCceyr7sTxTKydxtDTPwoFhdDwY8T3Tv'

    script = p2pkh_script(network, addr)

    txout = tx_output(network=network, value=Decimal(1.35),
                      n=1, script=script
                      )

    assert isinstance(txout, TxOut)


def test_nulldata_script():

    null = tx_output(network='tao',
                     value=Decimal(0), n=1,
                     script='Oh Hello.'.encode('utf-8'))

    assert isinstance(null, TxOut)


def test_p2pkh_script():

    addr = 'mvWDumZZZVD2nEC7hmsX8dMSHoGHAq5b6d'
    script = p2pkh_script('xto', addr)

    assert isinstance(script, P2pkhScript)


def test_make_raw_transaction():

    tx = make_raw_transaction("tao", [], [], Locktime(300000))
    assert isinstance(tx, MutableTransaction)


def test_sign_transaction():

    network_params = net_query('xto')

    provider = pa.Cryptoid(network='xto')
    key = pa.Kutil(network='xto',
                   privkey=bytearray.fromhex('4784326D5470603F569CF9BA257B7BAFD2A5D296AC61CEC44576FE7AD5EE0C7E')
                   )
    dest_address = pa.Kutil(network='xto').address
    unspent = provider.select_inputs(key.address, 1)

    output = tx_output(network='xto',
                       value=Decimal(0.1),
                       n=0, script=p2pkh_script(network='xto',
                                                address=dest_address)
                       )

    unsigned = TaoMutableTx(version=1,
                                 timestamp=int(time.time()),
                                 ins=unspent['utxos'],
                                 outs=[output],
                                 locktime=Locktime(0),
                                 data='',
                                 network=network_params
                                 )

    assert isinstance(sign_transaction(provider, unsigned, key), Transaction)
