import unittest
import yaml
import binascii
import sys
import json
from RecordsKeeperPythonLib import transaction
from RecordsKeeperPythonLib.transaction import Transaction

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

class TransactionTest(unittest.TestCase):


    def test_sendtransaction(self):
        
        txid = Transaction.sendTransaction(self, cfg['miningaddress'], cfg['validaddress'], "hello", cfg['amount'])
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)

    def test_sendrawtransaction(self):

        txid = Transaction.sendRawTransaction(self, cfg['dumpsignedtxhex'])
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)

    def test_signrawtransaction(self):

        txhex = Transaction.signRawTransaction(self, cfg['dumptxhex'], cfg['privatekey'])
        tx_size = sys.getsizeof(txhex)
        self.assertEqual(tx_size, 501)

    def test_createrawtransaction(self):

        txhex = Transaction.createRawTransaction(self, cfg['miningaddress'], cfg['validaddress'], cfg['amount'], net['testdata'])
        tx_size = sys.getsizeof(txhex)
        self.assertEqual(tx_size, 317)

    def test_sendsignedtransaction(self):

        txid = Transaction.sendSignedTransaction(self, cfg['miningaddress'], cfg['validaddress'] , cfg['amount'], net['privatekey'],net['testdata'])
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)


    def test_retrievetransaction(self):

        sentdata = Transaction.retrieveTransaction(self, cfg['dumptxid'])
        sent_data = json.loads(sentdata)
        data = sent_data['sent data']
        self.assertEqual(data, "hellodata")

    
    def test_getfee(self):

        fees = Transaction.getFee(self, cfg['miningaddress'], cfg['dumptxid'])
        self.assertGreaterEqual(fees, 0)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TransactionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
