# pytaoassets

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI](https://img.shields.io/pypi/v/pytaoassets.svg?style=flat-square)](https://pypi.python.org/pypi/pytaoassets/)
[![](https://img.shields.io/badge/python-3.5+-blue.svg)](https://www.python.org/download/releases/3.5.0/) 
[![Build Status](https://travis-ci.org/PeerAssets/pytaoassets.svg?branch=master)](https://travis-ci.org/PeerAssets/pytaoassets)
[![Coverage Status](https://coveralls.io/repos/github/PeerAssets/pytaoassets/badge.svg)](https://coveralls.io/github/PeerAssets/pytaoassets)

Official Python implementation of the [PeerAssets protocol](https://github.com/PeerAssets/WhitePaper) for the Tao Network.

`pytaoassets` aims to implement the PeerAssets protocol itself **and** to provide elementary interfaces to underlying blockchain(s).

## Examples

> import pytaoassets as pa

> provider = pa.Explorer(network='tppc')

> deck = pa.find_deck(provider, 'b6a95f94fef093ee9009b04a09ecb9cb5cba20ab6f13fe0926aeb27b8671df43', 1, True)

> print(deck.to_json())

## Running tests

> pytest-3 -v test/

### VirtualEnv Development

Create a python3 virtualenv in the root directory:

```
> virtualenv -p python3 venv
...
> source venv/bin/activate
(venv) > pip install -r requirements.txt
...
(venv) > pip install -r requirements-dev.txt
...
(venv) > pytest
...
```

`pytaoassets` is lovingly crafted with python3 all around the world :heart: :snake: :globe_with_meridians:
