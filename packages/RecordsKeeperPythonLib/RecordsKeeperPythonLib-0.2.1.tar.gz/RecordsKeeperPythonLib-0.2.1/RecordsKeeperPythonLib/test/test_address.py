import unittest
import yaml
import binascii
import sys
from RecordsKeeperPythonLib import address
from RecordsKeeperPythonLib.address import Address


with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

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

        address = Address.getMultisigWalletAddress(self, cfg['nrequired'], cfg['multisigpubkey'])
        self.assertEqual(address, cfg['multisigaddress'])

    def test_getmultisigaddress(self):

        address = Address.getMultisigAddress(self, cfg['nrequired'],  cfg['multisigpubkey'] )
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