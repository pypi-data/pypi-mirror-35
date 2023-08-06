import unittest
import yaml
import binascii
import json
from RecordsKeeperPython3Lib import stream
from RecordsKeeperPython3Lib.stream import Stream

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


class StreamTest(unittest.TestCase):


    def test_publish(self):
        
        txid = Stream.publish(self, cfg['miningaddress'], cfg['stream'], cfg['testdata'], "This is test data")
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)

    def test_retrieve_with_txid(self):

        result = Stream.retrieve(self, cfg['stream'], cfg['dumptxid'])
        self.assertIsNotNone(result)


    def test_retrieve_with_id_address(self):

        result = Stream.retrieveWithAddress(self, cfg['stream'], cfg['miningaddress'], 10)
        address = json.loads(result)
        publisher_key = address['key'][0]
        self.assertIsNotNone(publisher_key)
    
    def test_retrieve_with_key(self):

        result = Stream.retrieveWithKey(self, cfg['stream'], cfg['testdata'], 10)
        key = json.loads(result)
        publisher_data = key['data'][0]
        self.assertIsNotNone(publisher_data)

    def test_verifyData(self):

        result = Stream.verifyData(self, cfg['stream'], cfg['testdata'], 100)
        self.assertEqual(result, "Data is successfully verified.")

    def test_retrieveItems(self):
        
        result = Stream.retrieveItems(self, cfg['stream'], 10)
        items = json.loads(result)
        published_items = items['data'][0]
        self.assertIsNotNone(published_items)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(StreamTest)
    unittest.TextTestRunner(verbosity=2).run(suite)