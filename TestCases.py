import builtins
import io
import sys
import unittest
from unittest import mock
from unittest.mock import MagicMock
import main


class TestCases(unittest.TestCase):
    def test_wenn_eingabe_basisnetz_eingabe_richtig_dann_gebe_netzadresse_basisnetz_zurueck(self):
        with mock.patch('builtins.input', return_value="1.2.3.0"):
            assert main.eingabe_basisnetz() == "1.2.3.0"

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_eingabe_basisnetz_eingabe_falsch(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["ungültige Eingabe, die keine Zahl ist", "5"]):    # wird sonst endlos ausgeführt, daher noch eine gültige Eingabe
            main.eingabe_basisnetz()
            self.assertEqual(mock_stdout.getvalue(), "Fehlerhafte Eingabe\n")


# Anzahl der Subnetzmaske: Eingabe und Prüfung (es darf kein Text eingegeben werden und nicht zu HOhe Anzahl der Subnetze)
# Fehlermeldung bei z.B. zu vielen Netzen soll ausgegeben werden (128 subnetze (dafür keine Hosts, macht keinen Sinn), 64 subnetze (2 hosts))
    def test_wenn_eingabe_anz_subnetzmaske_richtig_dann_return_anz_subnetz(self):
        with mock.patch('builtins.input', return_value="5"):
            assert main.eingabe_anz_subnetzmaske() == 5

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_eingabe_anz_subnetzmaske_groeßer_als_64_dann_gib_fehlermeldung_aus(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["65", "64"]):                                    # wird sonst endlos ausgeführt, daher noch eine gültige Eingabe
            main.eingabe_anz_subnetzmaske()
            self.assertEqual(mock_stdout.getvalue(), "Bei so vielen Subnetzen können keine Host-Adressen mehr vergeben werden. Bitte gib eine geringere Subnetz-Anzahl an\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_eingabe_anz_subnetzmaske_kein_int_dann_gib_fehlermeldung_aus(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["ungültige Eingabe, die keine Zahl ist", "64"]): # wird sonst endlos ausgeführt, daher noch eine gültige Eingabe
            main.eingabe_anz_subnetzmaske()
            self.assertEqual(mock_stdout.getvalue(), "Fehlerhafte Eingabe\n")

    def test_teile_netzip_als_array(self):
        netzadresse_basisnetz = "1.2.3.0"
        self.assertEqual(main.teile_netzip_als_array(netzadresse_basisnetz), ['1', '2', '3', '0'])

    def test_wenn_berechne_bits_aus_hostpart_return_(self):
        anz_subnetz_as_int = 4
        self.assertEqual(main.berechne_bits_aus_hostpart(anz_subnetz_as_int), 2)

    def test_wenn_berechnung_anz_subnetze_hat_rest_dann_erhoehe_wert_und_gib_anz_subnetze_zurueck(self):
        log_anz_subnetz = 2.32
        self.assertEqual(main.berechnung_anz_subnetze(log_anz_subnetz), 3)

    def test_wenn_berechnung_anz_subnetze_hat_keinen_rest_dann_gib_anz_subnetze_zurueck(self):
        log_anz_subnetz = 3
        self.assertEqual(main.berechnung_anz_subnetze(log_anz_subnetz), 3)

    def test_wenn_berechnung_anz_host_gebe_anz_hosts_zurueck(self):     # (2 ^ (8 - log_anz_subnetz)) - 2
        log_anz_subnetz = 5
        self.assertEqual(main.berechnung_anz_host(log_anz_subnetz), 6)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_ausgabe_anz_host_gebe_anz_hosts_mit_Einleiungssatz_aus(self, mock_stdout):
        anz_hosts = 30
        main.ausgabe_anz_host(anz_hosts)
        self.assertEqual("\nAnzahl der Hosts pro Subnetz: 30\n", mock_stdout.getvalue())


    def test_wenn_berechnung_subnetzmaske_dann_return_subnetzmaske(self):
        log_anz_subnetz = 2
        self.assertEqual(main.berechnung_subnetzmaske(log_anz_subnetz), "192")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_ausgabe_subnetzmaske_dann_gib_subnetzmaske_mit_inhalt_aus(self, mock_stdout):
        log_anz_subnetz = 2
        main.ausgabe_subnetzmaske(log_anz_subnetz)
        self.assertEqual("Subnetzmaske: 255.255.255.192\n\n", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ausgabe_netzwerk_broadcast(self, mock_stdout):
        netz_ip = ['1','2','3','0']
        host_anz_subnetz = 128
        anz_subnetz = "2"
        main.ausgabe_netzwerk_broadcast(anz_subnetz, netz_ip, host_anz_subnetz)
        self.assertEqual("1. Subnetz:\nNetzwerkadresse: 1.2.3.0\nBroadcastadresse: 1.2.3.127\n\n"
                         "2. Subnetz:\nNetzwerkadresse: 1.2.3.128\nBroadcastadresse: 1.2.3.255\n\n", mock_stdout.getvalue())

    #for i in range(0, int(anz_subnetz)):
        # print(str(i + 1) + ". Subnetz:")
        # print(P))
    #         # print("Broadcastadresse: " + str(netzIP[0]) + "." + str(netzI[1]) + "." + str(netzIP[2]) + "." + str((int(netzIP[3]) + (i + 1) * host_anz_subnetz) - 1))
        # print()

    def test_wenn_erneute_berechnung_abfrage_ja_return_true(self):
        with mock.patch('builtins.input', return_value="Ja"):
            assert main.erneute_berechnung_abfrage() == True

    def test_wenn_erneute_berechnung_abfrage_nein_return_false(self):
        with mock.patch('builtins.input', return_value="Nein"):
            assert main.erneute_berechnung_abfrage() == False

    # Main-Methode testen?

if __name__ == '__main__':
    unittest.main()