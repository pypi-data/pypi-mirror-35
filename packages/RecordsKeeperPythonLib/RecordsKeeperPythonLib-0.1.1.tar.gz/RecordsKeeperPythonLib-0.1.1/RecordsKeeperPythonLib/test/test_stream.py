import unittest
import yaml
import binascii
import json
from RecordsKeeperPythonLib import stream
from RecordsKeeperPythonLib.stream import Stream

import sys

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

class StreamTest(unittest.TestCase):


    def test_publish(self):
        
        txid = Stream.publish(self, cfg['miningaddress'], cfg['stream'], cfg['testdata'], "This is test data")
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)

    def test_retrieve_with_txid(self):

        result = Stream.retrieve(self, cfg['stream'], cfg['dumptxid'])
        self.assertEqual(result,"testdata")


    def test_retrieve_with_id_address(self):

        result = Stream.retrieveWithAddress(self, cfg['stream'], cfg['miningaddress'], 10000)
        address = json.loads(result)
        publisher_key = address['key'][0]
        self.assertEqual(publisher_key, "key1")
    
    def test_retrieve_with_key(self):

        result = Stream.retrieveWithKey(self, cfg['stream'], cfg['testdata'], 10000)
        key = json.loads(result)
        publisher_data = key['data'][0]
        self.assertEqual(publisher_data, "This is test data")

    def test_verifyData(self):

        result = Stream.verifyData(self, cfg['stream'], cfg['testdata'], 10000)
        self.assertEqual(result, "Data is successfully verified.")

    def test_retrieveItems(self):
        
        result = Stream.retrieveItems(self, cfg['stream'], 10000)
        items = json.loads(result)
        published_items = items['data'][0]
        self.assertEqual(published_items, "data")
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(StreamTest)
    unittest.TextTestRunner(verbosity=2).run(suite)