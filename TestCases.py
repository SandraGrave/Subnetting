import builtins
import unittest
from unittest import mock
from unittest.mock import MagicMock
import main


class TestCases(unittest.TestCase):
    def test_wenn_eingabe_basisnetz_eingabe_richtig_dann_gebe_netzadresse_basisnetz_zurueck(self):
        with mock.patch('builtins.input', return_value="1.2.3.0"):
            assert main.eingabe_basisnetz() == "1.2.3.0"




    #def test_eingabe_basisnetz_eingabe_falsch(self):
    #    self.assertEqual(True, False)


    def test_teile_netzip_als_array(self):
        netzadresse_basisnetz = "1.2.3.0"
        self.assertEqual(main.teile_netzip_als_array(netzadresse_basisnetz), ['1', '2', '3', '0'])





if __name__ == '__main__':
    unittest.main()
