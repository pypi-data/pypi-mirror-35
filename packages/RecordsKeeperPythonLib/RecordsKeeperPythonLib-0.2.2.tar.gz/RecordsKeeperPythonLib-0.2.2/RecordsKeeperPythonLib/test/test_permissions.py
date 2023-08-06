import unittest
import yaml
import binascii
from RecordsKeeperPythonLib import permissions
from RecordsKeeperPythonLib.permissions import Permissions

import sys

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

class PermissionsTest(unittest.TestCase):


    def test_grantpermissions(self):
        
        txid = Permissions.grantPermission(self, cfg['permissionaddress'], "create, connect")
        self.assertEqual(txid, 'Invalid permission')

    def test_revokepermissions(self):

        txid = Permissions.revokePermission(self, cfg['permissionaddress'], "send, admin")
        self.assertEqual(txid, 'Invalid permission')


    def test_failgrantpermissions(self):

    	txid = Permissions.grantPermission(self, cfg['permissionaddress'], "create, connect")
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)


    def test_failrevokepermissions(self):

    	txid = Permissions.revokePermission(self, cfg['permissionaddress'], "create, connect")
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PermissionsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)