import unittest
import yaml
import json
from RecordsKeeperPythonLib import block
from RecordsKeeperPythonLib.block import Block

import sys


with open("config.yaml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile)

class BlockTest(unittest.TestCase):

    def test_block_info(self):

        miner = Block.blockinfo(self, "100")
        miner_address = json.loads(miner)
        miner_add = miner_address['miner']  
        self.assertEqual(miner_add, cfg['mainaddress'])
        
        size = Block.blockinfo(self, "100")
        block_size = json.loads(size)
        blocksize = block_size['size']
        self.assertGreaterEqual(blocksize, 280)


    def test_retrieveBlocks(self):

        miner = Block.retrieveBlocks(self, "10-20")
        miner_address = json.loads(miner)
        mineraddress = miner_address['miner'][0]
        self.assertEqual(mineraddress, cfg['mainaddress'])

        txcount = Block.retrieveBlocks(self, "10-20")
        tx_count = json.loads(txcount)
        blocktxcount = tx_count['tx count'][0]
        self.assertGreaterEqual(blocktxcount, 1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BlockTest)
    unittest.TextTestRunner(verbosity=2).run(suite)