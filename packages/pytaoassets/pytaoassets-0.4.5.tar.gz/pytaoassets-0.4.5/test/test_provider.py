import pytest

from pytaoassets.provider import Cryptoid, Explorer


@pytest.mark.parametrize("provider_cls", [Cryptoid, Explorer])
def test_validateaddress_peercoin(provider_cls):
    "Check Providers that can validate Tao addresses."

    provider = provider_cls(network='tao')

    # Peercoin P2PKH, P2SH addresses.
    assert provider.validateaddress("TqSeQRAiH4tkECbtFdR99ytE2AysUYqhEf") is True
    assert provider.validateaddress("2USHRW8UcSAAnHxWnPe4yX2BV5K3dbWss9") is True

    # Peercoin Testnet P2PKH address (these _should_ be False).
    assert provider.validateaddress("mj46gUeZgeD9ufU7Fvz2dWqaX6Nswtbpba") is False
    assert provider.validateaddress("n12h8P5LrVXozfhEQEqg8SFUmVKtphBetj") is False

    # Very much not Peercoin addresses.
    assert provider.validateaddress("1BFQfjM29kubskmaAsPjPCfHYphYvKA7Pj") is False
    assert provider.validateaddress("2NFNPUYRpDXf3YXEuVT6AdMesX4kyeyDjtp") is False


