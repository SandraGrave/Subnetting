import builtins
import io
import sys
import unittest
from unittest import mock
from unittest import mock, TestCase
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

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_eingabe_der_subnetz_maske_unter_8(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["7", "8"]):                                        # wird sonst endlos ausgeführt, daher noch eine gültige Eingabe
            main.eingabe_der_subnetz_maske()
            self.assertEqual(mock_stdout.getvalue(), "Du brauchst mindestens einen Präfix von 8\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_eingabe_der_subnetz_maske_ueber_30(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["30", "29"]):                                      # wird sonst endlos ausgeführt, daher noch eine gültige Eingabe
            main.eingabe_der_subnetz_maske()
            self.assertEqual(mock_stdout.getvalue(), "Bei über 29 Subnetzen können keine Hosts mehr vergeben werden, bitte gib eine geringe Anzahl an\n")


# Anzahl der Subnetzmaske: Eingabe und Prüfung (es darf kein Text eingegeben werden und nicht zu Hohe Anzahl der Subnetze)
    def test_wenn_eingabe_anz_subnetzmaske_richtig_dann_return_anz_subnetz(self):
        with mock.patch('builtins.input',  return_value="50"):
            freie_subnetz_stellen = 8
            assert main.eingabe_anz_subnetzmaske(freie_subnetz_stellen) <= 256

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_eingabe_anz_subnetzmaske_groeßer_als_moeglich_dann_gib_fehlermeldung_aus(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["265", "64"]):                                    # wird sonst endlos ausgeführt, daher noch eine gültige Eingabe
            freie_subnetz_stellen = 8
            main.eingabe_anz_subnetzmaske(freie_subnetz_stellen)
            self.assertEqual(mock_stdout.getvalue(), "Bei so vielen Subnetzen können keine Host-Adressen mehr vergeben werden. Bitte gib eine geringere Subnetz-Anzahl an, das Maximum an möglichen Netzen ist: 256\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_eingabe_anz_subnetzmaske_kleiner_als_moeglich_dann_gib_fehlermeldung_aus(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["0", "64"]):                                     # wird sonst endlos ausgeführt, daher noch eine gültige Eingabe
            freie_subnetz_stellen = 8
            main.eingabe_anz_subnetzmaske(freie_subnetz_stellen)
            self.assertEqual(mock_stdout.getvalue(), "Bitte gib keine Zahl unter 2 oder negativen Zahlen ein\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_eingabe_anz_subnetzmaske_kein_int_dann_gib_fehlermeldung_aus(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["ungültige Eingabe, die keine Zahl ist", "64"]): # wird sonst endlos ausgeführt, daher noch eine gültige Eingabe
            freie_subnetz_stellen = 8
            main.eingabe_anz_subnetzmaske(freie_subnetz_stellen)
            self.assertEqual(mock_stdout.getvalue(), "Fehlerhafte Eingabe\n")


    def test_validiere_zahl_zwischen_ist_gueltige_eingabe(self):
        with mock.patch('builtins.input', return_value="12"):
            min = 2
            max = 29
            fehler_min = "Fehlermeldung Min"
            fehler_max = "Fehlermeldung Max"
            frage = "Wie viele Bits sind als Netzwerkpart gewünscht? (min 8, max 29): "
            assert main.validiere_zahl_zwischen(min, max, fehler_min, fehler_max, frage) == 12


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_validiere_zahl_zwischen_ist_keine_Zahl(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["ungültige Eingabe, die keine Zahl ist", "12"]):
            min = 2
            max = 29
            fehler_min = "Fehlermeldung Min"
            fehler_max = "Fehlermeldung Max"
            frage = "Wie viele Bits sind als Netzwerkpart gewünscht? (min 8, max 29): "
            main.validiere_zahl_zwischen(min, max, fehler_min, fehler_max, frage)
            self.assertEqual(mock_stdout.getvalue(), "Fehlerhafte Eingabe\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_validiere_zahl_zwischen_ist_unter_minimum(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["1", "12"]):
            min = 2
            max = 29
            fehler_min = "Fehlermeldung Min"
            fehler_max = "Fehlermeldung Max"
            frage = "Wie viele Bits sind als Netzwerkpart gewünscht? (min 8, max 29): "
            main.validiere_zahl_zwischen(min, max, fehler_min, fehler_max, frage)
            self.assertEqual(mock_stdout.getvalue(), "Fehlermeldung Min\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_validiere_zahl_zwischen_ist_ueber_maximum(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=["30", "12"]):
            min = 2
            max = 29
            fehler_min = "Fehlermeldung Min"
            fehler_max = "Fehlermeldung Max"
            frage = "Wie viele Bits sind als Netzwerkpart gewünscht? (min 8, max 29): "
            main.validiere_zahl_zwischen(min, max, fehler_min, fehler_max, frage)
            self.assertEqual(mock_stdout.getvalue(), "Fehlermeldung Max\n")

    def test_teile_netzip_als_array(self):
        netzadresse_basisnetz = "1.2.3.0"
        self.assertEqual(main.teile_netzip_als_array(netzadresse_basisnetz), ['1', '2', '3', '0'])


    def test_wenn_berechne_bits_aus_hostpart_return_ergebnis(self):
        anz_subnetz_as_int = 4
        self.assertEqual(main.berechne_bits_aus_hostpart(anz_subnetz_as_int), 2)

    def test_wenn_berechnung_anz_subnetze_hat_rest_dann_erhoehe_wert_und_gib_anz_subnetze_zurueck(self):
        log_anz_subnetz = 2.32
        self.assertEqual(main.berechnung_anz_subnetze(log_anz_subnetz), 3)

    def test_wenn_berechnung_anz_subnetze_hat_0_als_kommastellen_dann_erhoehe_wert_nicht_und_gib_anz_subnetze_ohne_kommastellen_zurueck(self):
        log_anz_subnetz = 2.00
        self.assertEqual(main.berechnung_anz_subnetze(log_anz_subnetz), 2)

    def test_wenn_berechnung_anz_subnetze_hat_keinen_rest_dann_gib_anz_subnetze_zurueck(self):
        log_anz_subnetz = 3
        self.assertEqual(main.berechnung_anz_subnetze(log_anz_subnetz), 3)

    def test_wenn_berechnung_anz_host_korrekt_gebe_anzahl_zurueck(self):     # (2 ^ (anz_bits_subnetz - log_anz_subnetz) - 2
        log_anz_subnetz = 5
        anz_bits_subnetz = 8
        self.assertEqual(main.berechnung_anz_host(log_anz_subnetz, anz_bits_subnetz), 6)


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_ausgabe_anz_host_gebe_anz_hosts_mit_Einleiungssatz_aus(self, mock_stdout):
        anz_hosts = 30
        main.ausgabe_anz_host(anz_hosts)
        self.assertEqual("\nAnzahl der Hosts pro Subnetz: 30\n", mock_stdout.getvalue())


    def test_wenn_berechnung_subnetzmaske_mit_22_freien_und_6_belegten_stellen_gebe_subnetz_maske_zurueck(self):
        anz_bits_subnetzpart = 6
        freie_bits_hostpart = 22
        self.assertEqual(main.berechnung_subnetzmaske(anz_bits_subnetzpart, freie_bits_hostpart), 0b11111111111111110000000000000000)   # = 11111111 11111111 00000000 00000000

    def test_wenn_berechnung_subnetzmaske_mit_0_freien_und_0_belegten_stellen_gebe_subnetz_maske_zurueck(self): # = 24 Stellen für Netzwerk-Part zur Verfügung, davon 0 Stellen für Hostpart frei
        anz_bits_subnetzpart = 0
        freie_bits_hostpart = 0
        self.assertEqual(main.berechnung_subnetzmaske(anz_bits_subnetzpart, freie_bits_hostpart), 0b11111111111111111111111111111111)   # = 11111111 11111111 11111111 11111111

    def test_wenn_berechnung_subnetzmaske_mit_24_freien_und_24_belegten_stellen_gebe_subnetz_maske_zurueck(self):
        anz_bits_subnetzpart = 24
        freie_bits_hostpart = 24
        self.assertEqual(main.berechnung_subnetzmaske(anz_bits_subnetzpart, freie_bits_hostpart), 0b11111111111111111111111111111111)   # = 11111111 11111111 11111111 11111111

    def test_wenn_berechnung_subnetzmaske_mit_24_ferien_und_0_belegten_stellen_gebe_subnetz_maske_zurueck(self):
        anz_bits_subnetzpart = 0
        freie_bits_hostpart = 24
        self.assertEqual(main.berechnung_subnetzmaske(anz_bits_subnetzpart, freie_bits_hostpart), 0b11111111000000000000000000000000)   # = 11111111 00000000 00000000 00000000

    def test_umwandlung_int_32_zu_subnetzmaske(self):
        subnetzmaske = 0b11111111000000000000000000000000           # = 11111111 00000000 00000000 00000000
        self.assertEqual(main.umwandlung_int_32_zu_subnetzmaske(subnetzmaske), "255.0.0.0")


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wenn_ausgabe_subnetzmaske_gebe_subnetzmaske_mit_einleitungssatz_aus(self, mock_stdout):
        subnetzmaske_as_string = "255.255.255.0"
        main.ausgabe_subnetzmaske(subnetzmaske_as_string)
        self.assertEqual("Subnetzmaske: 255.255.255.0\n\n", mock_stdout.getvalue())

    def test_umwandlung_subnetzmaske_zu_int_32(self):
        netz_ip =['255', '255', '128', '0']
        self.assertEqual(main.umwandlung_subnetzmaske_zu_int_32(netz_ip), 0b11111111111111111000000000000000)   # = 11111111 11111111 10000000 00000000


    def test_erstelle_bitmaske_netzwerkpart(self):  # Anzahl der Bits für Netzwerkpart, 1en werden gesetzt
        freie_bits_hostpart = 8
        self.assertEqual(main.erstelle_bitmaske_netzwerkpart(freie_bits_hostpart), 0b11111111111111111111111100000000)  # = 11111111 1111111 111111111 00000000


    def test_berechnung_netzwerk_broadcast(self):
        with mock.patch('main.erstelle_bitmaske_netzwerkpart', side_effect=[0b11111111111111111111111100000000]), \
                mock.patch('main.berechnung_netzwerk_adresse', side_effect=["255.128.3.0", "255.128.3.128"]), \
                mock.patch('main.berechnung_broadcast_adresse', side_effect=["255.128.3.127", "255.128.3.255"]):
            anz_subnetz = 2
            netz_ip_as_int = 0b1111111110000000000001100000000  # = 255.128.3.0
            freie_bits_hostpart = 8
            self.assertEqual(main.berechnung_netzwerk_broadcast(anz_subnetz, netz_ip_as_int, freie_bits_hostpart), [['255.128.3.0', '255.128.3.128'], ['255.128.3.127', '255.128.3.255']])


    #@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    #def test_wenn_ausgabe_netzwerk_broadcast_gebe_beides_aus(self, mock_stdout):
    #    netzwerkadressen_liste = [['255.0.0.0', '255.8.0.0', '255.16.0.0', '255.24.0.0']]
    #    main.ausgabe_netzwerk_broadcast(netzwerkadressen_liste)
    #    self.assertEqual("1. Subnetz:\nNetzwerkadresse: 255.0.0.0\nBroadcastadresse: 255.7.255.255\n\n"
    #                     "2. Subnetz:\nNetzwerkadresse: 255.8.0.0\nBroadcastadresse: 255.15.255.255\n\n"
    #                     "3. Subnetz:\nNetzwerkadresse: 255.16.0.0\nBroadcastadresse: 255.23.255.255\n\n"
    #                     "4. Subnetz:\nNetzwerkadresse: 255.24.0.0\nBroadcastadresse: 255.31.255.255\n\n", mock_stdout.getvalue())

# '255.32.0.0', '255.40.0.0', '255.48.0.0', '255.56.0.0', '255.64.0.0', '255.72.0.0', '255.80.0.0', '255.88.0.0', '255.96.0.0', '255.104.0.0', '255.112.0.0', '255.120.0.0', '255.128.0.0', '255.136.0.0', '255.144.0.0', '255.152.0.0', '255.160.0.0', '255.168.0.0', '255.176.0.0', '255.184.0.0', '255.192.0.0', '255.200.0.0', '255.208.0.0', '255.216.0.0', '255.224.0.0', '255.232.0.0', '255.240.0.0', '255.248.0.0'], ['255.7.255.255', '255.15.255.255', '255.23.255.255', '255.31.255.255', '255.39.255.255', '255.47.255.255', '255.55.255.255', '255.63.255.255', '255.71.255.255', '255.79.255.255', '255.87.255.255', '255.95.255.255', '255.103.255.255', '255.111.255.255', '255.119.255.255', '255.127.255.255', '255.135.255.255', '255.143.255.255', '255.151.255.255', '255.159.255.255', '255.167.255.255', '255.175.255.255', '255.183.255.255', '255.191.255.255', '255.199.255.255', '255.207.255.255', '255.215.255.255', '255.223.255.255', '255.231.255.255', '255.239.255.255', '255.247.255.255', '255.255.255.255'


    def test_wenn_erneute_berechnung_abfrage_ja_return_true(self):
        with mock.patch('builtins.input', return_value="Ja"):
            assert main.erneute_berechnung_abfrage() == True


    def test_wenn_erneute_berechnung_abfrage_nein_return_false(self):
        with mock.patch('builtins.input', return_value="Nein"):
            assert main.erneute_berechnung_abfrage() == False

    # Main-Methode testen?

if __name__ == '__main__':
    unittest.main()