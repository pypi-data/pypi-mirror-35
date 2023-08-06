import unittest
import yaml
import binascii
import sys
import json
from RecordsKeeperPython3Lib import wallet
from RecordsKeeperPython3Lib.wallet import Wallet

import os.path

if (os.path.exists("config.yaml")):
   with open("config.yaml", 'r') as ymlfile:
      cfg = yaml.load(ymlfile)

      url = cfg['url']
      user = cfg['rkuser']
      password = cfg['passwd']
      chain = cfg['chain']

else:
   
   url = os.environ['url']
   user = os.environ['rkuser']
   password = os.environ['passwd']
   chain = os.environ['chain']

   
class WalletTest(unittest.TestCase):

    def test_createwallet(self):
        
        address = Wallet.createWallet(self)
        add = json.loads(address)
        add1 = add['public address']
        address_size = sys.getsizeof(add1)
        self.assertEqual(address_size, 83)

    def test_getprivkey(self):

        checkprivkey = Wallet.getPrivateKey(self, cfg['miningaddress'])
        self.assertEqual(checkprivkey, cfg['privatekey'])

    def test_retrievewalletinfo(self):

        wallet_balance = Wallet.retrieveWalletinfo(self)
        balance = json.loads(wallet_balance)
        walletbalance = balance['balance']
        self.assertGreaterEqual(wallet_balance, '0')

    def test_signmessage(self):

        signedMessage = Wallet.signMessage(self, cfg['privatekey'], cfg['testdata'])
        self.assertEqual(signedMessage, cfg['signedtestdata'])

    def test_verifymessage(self):

        validity = Wallet.verifyMessage(self, cfg['miningaddress'], cfg['signedtestdata'], cfg['testdata'])
        self.assertEqual(validity, 'Yes, message is verified')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WalletTest)
    unittest.TextTestRunner(verbosity=2).run(suite)