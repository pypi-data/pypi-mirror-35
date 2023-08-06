import unittest
import yaml
import binascii
from RecordsKeeperPython3Lib import address
from RecordsKeeperPython3Lib.address import Address


import sys

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


class AddressTest(unittest.TestCase):

    def test_getaddress(self):
        
        address = Address.getAddress(self)
        address_size = sys.getsizeof(address)
        self.assertEqual(address_size, 83)

    def test_checkifvalid(self):

        checkaddress = Address.checkifValid(self, cfg['validaddress'])
        self.assertEqual(checkaddress, 'Address is valid')

    def test_failcheckifvalid(self):

        wrongaddress = Address.checkifValid(self, cfg['invalidaddress'])
        self.assertEqual(wrongaddress, 'Address is valid')

    def test_checkifmineallowed(self):

        checkaddress = Address.checkifMineAllowed(self, cfg['miningaddress'])
        self.assertEqual(checkaddress, 'Address has mining permission')

    def test_failcheckifmineallowed(self):

        wrongaddress = Address.checkifMineAllowed(self, cfg['nonminingaddress'])
        self.assertEqual(wrongaddress, 'Address has mining permission')

    def test_checkbalance(self):

        balance = Address.checkBalance(self, cfg['nonminingaddress'])
        self.assertGreaterEqual(balance, 0)

    def test_getmultisigwalletaddress(self):

        address = Address.getMultisigWalletAddress(self, 2, "1Hz4LNyw29vp1sJvmya2KYR9tEfoNQ1G8bVvP3,1aj3G4tK9JkiD4XgjET3M7bzvfrLXQ5tRJn86R,1MQjnwpg6xVFm2TRfFTwXHVSzMN1g8yjp7CaJg")
        self.assertEqual(address, cfg['multisigaddress'])

    def test_getmultisigaddress(self):

        address = Address.getMultisigAddress(self, 2,  "1Hz4LNyw29vp1sJvmya2KYR9tEfoNQ1G8bVvP3,1aj3G4tK9JkiD4XgjET3M7bzvfrLXQ5tRJn86R,1MQjnwpg6xVFm2TRfFTwXHVSzMN1g8yjp7CaJg" )
        self.assertEqual(address, cfg['multisigaddress'])

    def test_importaddress(self):

        address = Address.importAddress(self, cfg['miningaddress'])
        self.assertEqual(address, "Address successfully imported")

    def test_wrongimportaddress(self):

        address = Address.importAddress(self, cfg['wrongimportaddress'])
        self.assertEqual(address, "Invalid Rk address or script")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AddressTest)
    unittest.TextTestRunner(verbosity=2).run(suite)