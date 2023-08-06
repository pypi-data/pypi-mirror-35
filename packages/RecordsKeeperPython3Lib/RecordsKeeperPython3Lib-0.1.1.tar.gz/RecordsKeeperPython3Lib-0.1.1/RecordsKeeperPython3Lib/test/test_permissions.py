import unittest
import yaml
import binascii
from RecordsKeeperPython3Lib import permissions
from RecordsKeeperPython3Lib.permissions import Permissions

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


class PermissionsTest(unittest.TestCase):


    def test_grantpermissions(self):
        
        txid = Permissions.grantPermission(self, cfg['permissionaddress'], "create,connect")
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)

    def test_revokepermissions(self):

        txid = Permissions.revokePermission(self, cfg['permissionaddress'], "create,connect")
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)


    def test_failgrantpermissions(self):

    	txid = Permissions.grantPermission(self, cfg['permissionaddress'], "create,connect")
    	tx_size = sys.getsizeof(txid)
    	self.assertNotEqual(tx_size, 113)


    def test_failrevokepermissions(self):

    	txid = Permissions.revokePermission(self, cfg['permissionaddress'], "create,connect")
    	tx_size = sys.getsizeof(txid)
    	self.assertNotEqual(tx_size, 113)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PermissionsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)