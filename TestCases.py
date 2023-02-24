import builtins
import unittest
from unittest import mock
from unittest.mock import MagicMock
import main


class TestCases(unittest.TestCase):
    def test_wenn_eingabe_basisnetz_eingabe_richtig_dann_gebe_netzadresse_basisnetz_zurueck(self):
        with mock.patch('builtins.input', return_value="1.2.3.0"):
            assert main.eingabe_basisnetz() == "1.2.3.0"

   # def test_eingabe_basisnetz_eingabe_falsch(self):
   #     with mock.patch('builtins.input', return_value="ungültige Eingabe wird eingegeben"):               # wird endlos ausgeführt, Ergebnis aber richtig
   #     assert main.eingabe_basisnetz() == "Fehlerhafte Eingabe"




# Anzahl der Subnetzmaske: Eingabe und Prüfung (es darf kein Text eingegeben werden und nicht zu HOhe Anzahl der Subnetze)
# Fehlermeldung bei z.B. zu vielen Netzen soll ausgegeben werden (128 subnetze (dafür keine Hosts, macht keinen Sinn), 64 subnetze (2 hosts))
    def test_wenn_eingabe_anz_subnetzmaske_richtig_dann_return_anz_subnetz(self):
        with mock.patch('builtins.input', return_value="5"):
            assert main.eingabe_anz_subnetzmaske() == 5


    #def test_wenn_eingabe_anz_subnetzmaske_groeßer_als_64_dann_gib_fehlermeldung_aus(self):                    # wird endlos ausgeführt, rgebnis aber richtig
    #    with mock.patch('builtins.input', return_value="65"):
    #        assert main.eingabe_anz_subnetzmaske() == "Bei so vielen Subnetzen können keine Host-Adressen mehr vergeben werden. Bitte gib eine geringere Subnetz-Anzahl an"


    def test_wenn_eingabe_anz_subnetzmaske_kein_int_dann_gib_fehlermeldung_aus(self):                           # wird endlos ausgeführt, Ergebnis aber richtig
        with mock.patch('builtins.input', return_value="ungültige EIngabe, die keine Zahl ist"):
            assert main.eingabe_anz_subnetzmaske() == "Fehlerhafte Eingabe"

    def test_teile_netzip_als_array(self):
        netzadresse_basisnetz = "1.2.3.0"
        self.assertEqual(main.teile_netzip_als_array(netzadresse_basisnetz), ['1', '2', '3', '0'])


    # def test_wenn_berechne_bits_aus_hostpart_return_(self):                                   # Methode kommt von Python, muss man sowas testen?
    #    anz_subnetz_as_int = 5
    #   self.assertEqual(main.berechne_bits_aus_hostpart(anz_subnetz_as_int), )




    # def test_berechnung_anz_subnetze(log_anz_subnetz):
    # if (log_anz_subnetz % 1) != 0:
    #    return int(log_anz_subnetz) + 1
    # else:
    #    return int(log_anz_subnetz)


    # def test_berechnung_anz_host(log_anz_subnetz):
    # host_anz_subnetz = pow(2, 8 - log_anz_subnetz)
    # return host_anz_subnetz - 2


    # def test_ausgabe_anz_host(anz_hosts):
    # print()
    # print("Anzahl der Hosts im jeweiligen Subnetz: " + str(anz_hosts))


    # def test_wenn_berechnung_subnetzmaske_dann_return_subnetzmaske(log_anz_subnetz):
    # subnetzmaske = 0
    # for i in range(0, log_anz_subnetz):
    #    subnetzmaske = subnetzmaske + (1<<(7-i))
    # return str(subnetzmaske)


    # def test_wenn_ausgabe_subnetzmaske_dann_gib_subnetzmaske_mit_inhalt_aus(log_anz_subnetz):
    # print("Subnetzmaske: 255.255.255." + berechnung_subnetzmaske(log_anz_subnetz))
    # print()


    # def test_ausgabe_netzwerk_broadcast(anz_subnetz, netzIP, host_anz_subnetz):
    #for i in range(0, int(anz_subnetz)):
        # print(str(i + 1) + ". Subnetz:")
        # print("Netzwerkadresse: " + str(netzIP[0]) + "." + str(netzIP[1]) + "." + str(netzIP[2]) + "." + str(int(netzIP[3]) + i * host_anz_subnetz))
        # print("Broadcastadresse: " + str(netzIP[0]) + "." + str(netzIP[1]) + "." + str(netzIP[2]) + "." + str((int(netzIP[3]) + (i + 1) * host_anz_subnetz) - 1))
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