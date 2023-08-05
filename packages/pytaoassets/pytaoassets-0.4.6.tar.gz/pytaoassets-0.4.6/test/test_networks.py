import pytest

from pytaoassets.exceptions import UnsupportedNetwork
from pytaoassets.networks import net_query


def test_net_query():
    "Check that we can find NetworkParams for networks by name."

    # Use a network's long name
    net_params = net_query("tao")
    assert net_params.shortname == "xto"

    # Use a network's short name
    net_params = net_query("xto")
    assert net_params.name == "tao"

    # Try to find a network we don't know about.
    with pytest.raises(UnsupportedNetwork):
        net_query("not a network name we know of.")
