
'''Communicate with local or remote peercoin-daemon via JSON-RPC'''

from operator import itemgetter
from .common import Provider
from pytaoassets.exceptions import InsufficientFunds
from taopy.structs.transaction import MutableTxIn, Sequence, ScriptSig
from decimal import Decimal, getcontext
getcontext().prec = 6

try:
    #from peercoin_rpc import Client
    from taorpc.authproxy import AuthServiceProxy, JSONRPCException
except:
    raise EnvironmentError("taorpc library is required for this to work,\
                            use pip to install it.")

class Client:
    '''JSON-RPC Client.'''

    def __init__(self, testnet=False, username=None, password=None,
                 ip=None, port=None, directory=None):

        if not ip:
            self.ip = 'localhost'  # default to localhost
        else:
            self.ip = ip

        if not username and not password:
            if not directory:
                try:
                    self.username, self.password = self.userpass()  # try to read from ~/.ppcoin
                except:
                    self.username, self.password = self.userpass(dir='Tao')  # try to read from ~/.peercoin
            else:
                self.username, self.password = self.userpass(dir=directory)  # try some other directory

        else:
            self.username = username
            self.password = password
        if testnet is True:
            self.testnet = True
            self.port = 9904
            self.url = 'http://{0}:{1}'.format(self.ip, self.port)
        else:
            self.testnet = False
            self.port = 15151
            self.url = 'http://{0}:{1}'.format(self.ip, self.port)
        if port is not None:
            self.port = port
            self.url = 'http://{0}:{1}'.format(self.ip, self.port)

        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        self.session.headers.update({'content-type': 'application/json'})

    def userpass(self, dir='Tao'):
        '''Reads config file for username/password'''

        source = os.path.expanduser('~/.{0}/{0}.conf').format(dir)
        dest = open(source, 'r')
        with dest as conf:
            for line in conf:
                if line.startswith('rpcuser'):
                    username = line.split("=")[1].strip()
                if line.startswith("rpcpassword"):
                    password = line.split("=")[1].strip()

        return username, password

    def req(self, method, params=()):
        """send request to ppcoind"""

        response = self.session.post(self.url,
                   data=json.dumps({"method": method,
                                    "params": params,
                                    "jsonrpc": "1.1"})
                ).json()

        if response["error"] is not None:
            return response["error"]
        else:
            return response["result"]

    def batch(self, reqs: list ):
        """ send batch request using jsonrpc 2.0 """

        batch_data = []

        for req_id, req in enumerate(reqs):
            batch_data.append( {"method": req[0], "params": req[1], "jsonrpc": "2.0", "id": req_id} )

        data = json.dumps(batch_data)
        response = self.session.post(self.url, data=data).json()
        return response

class RpcNode(Client, Provider):
    '''JSON-RPC connection to local Peercoin node'''

    def select_inputs(self, address: str, amount: int) -> dict:
        '''finds apropriate utxo's to include in rawtx, while being careful
        to never spend old transactions with a lot of coin age.
        Argument is intiger, returns list of apropriate UTXO's'''

        utxos = []
        utxo_sum = Decimal(-0.01)  # starts from negative due to minimal fee
        for tx in sorted(self.listunspent(address=address), key=itemgetter('confirmations')):

            if tx["address"] not in (self.pa_parameters.P2TH_addr,
                                     self.pa_parameters.test_P2TH_addr):

                utxos.append(
                        MutableTxIn(txid=tx['txid'],
                                    txout=tx['vout'],
                                    sequence=Sequence.max(),
                                    script_sig=ScriptSig.empty())
                         )

                utxo_sum += Decimal(tx["amount"])
                if utxo_sum >= amount:
                    return {'utxos': utxos, 'total': utxo_sum}

        if utxo_sum < amount:
            raise InsufficientFunds("Insufficient funds.")

        raise Exception("undefined behavior :.(")

    @property
    def is_testnet(self) -> bool:
        '''check if node is configured to use testnet or mainnet'''

        if self.getinfo()["testnet"] is True:
            return True
        else:
            return False

    @property
    def network(self) -> str:
        '''return which network is the node operating on.'''

        if self.is_testnet:
            return "xto"
        else:
            return "xto"

    def listunspent(
        self,
        address: str="",
        minconf: int=1,
        maxconf: int=999999,
    ) -> list:
        '''list UTXOs
        modified version to allow filtering by address.
        '''
        if address:
            return self.req("listunspent", [minconf, maxconf, [address]])

        return self.req("listunspent", [minconf, maxconf])
