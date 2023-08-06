import unittest
import yaml
import binascii
import json
from RecordsKeeperPython3Lib import assets
from RecordsKeeperPython3Lib.assets import Assets

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

class AssetsTest(unittest.TestCase):


    def test_createasset(self):
        
        txid = Assets.createAsset(self, cfg['validaddress'], "xyz", 100)
        self.assertEqual(txid, "Asset or stream with this name already exists")

    def test_sendasset(self):
        
        txid = Assets.sendAsset(self, cfg['validaddress'], "xyz", 100)
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)

    def test_retrieveassets1(self):

        txid = Assets.retrieveAssets(self)
        tx_id = json.loads(txid)
        txid1 = tx_id['id'][0]
        tx_size = sys.getsizeof(txid1)
        self.assertEqual(tx_size, 113)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AssetsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)