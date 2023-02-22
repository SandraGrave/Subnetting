import math
import re

# Berechnung Subnetzmaske: (selbst berechnen)
def berechnung_subnetzmaske(log_anz_subnetz):
    subnetzmaske = 0
    for i in range(0, log_anz_subnetz):
        subnetzmaske = subnetzmaske + (1<<(7-i))
    return str(subnetzmaske)

if __name__ == '__main__':
    wiederholen = True

    while (wiederholen == True):

        # Basisnetz-Adresse: Eingabe und Prüfung (es darf kein Text eingegeben werden.)
        validEntry = False
        while(validEntry == False):
            netzadresse_basisnetz = input("Bitte gib die Basisnetz-Adresse ein (x.x.x.x): ")
            netzadresse_basisnetz_ohne_Punkte = netzadresse_basisnetz.replace(".", "")
            if netzadresse_basisnetz_ohne_Punkte.isdigit():
                validEntry = True
            else:
                print("Fehlerhafte Eingabe")

        # Anzahl der Subnetzmaske: Eingabe und Prüfung (es darf kein Text eingegeben werden.)
        validEntry = False
        while (validEntry == False):
            anz_subnetz = input("Wie viele Subnetze sind gewünscht?: ")
            if anz_subnetz.isdigit():                 # Prüfung, ob int
                validEntry = True
            else:
                print("Fehlerhafte Eingabe")

        # Fehlermeldung bei z.B. zu vielen Netzen soll ausgegeben werden (128 subnetze (dafür keine Hosts), 64 subnetze (2 hosts))
        #
        #
        #
        #

        anz_subnetz_as_int = int(anz_subnetz)
        netzIP = netzadresse_basisnetz.split(".")

        # Wie viele Bits vom Host-Part müssen wir für den Netzwerkbereich klauen?
        log_anz_subnetz = math.log2(anz_subnetz_as_int)

        # actual_number_of_subnets = math.ceil(log_number_of_subnets)     # Aufrunden von anzahl_subnetz
        # print(actual_number_of_subnets)

        # Wie viele Subnetze müssen erstellt werden?
        if (log_anz_subnetz % 1) != 0:
            log_anz_subnetz = int(log_anz_subnetz) + 1
        else:
            log_anz_subnetz = int(log_anz_subnetz)

        # Berechnung Anzahl der möglichen Hosts pro Subnetz
        host_anz_subnetz = pow(2, 8 - log_anz_subnetz)
        anz_hosts = host_anz_subnetz - 2
        print()
        print("Anzahl der Hosts im jeweiligen Subnetz: " + str(anz_hosts))

        print("Subnetzmaske: 255.255.255." + berechnung_subnetzmaske(log_anz_subnetz))
        print()

        # evtl. später bei flexibler Subnetzmaske:
        #erstes_oktett_binaer = (bin(int(netzIP[0])))
        #zweites_oktett_binaer = (bin(int(netzIP[1])))
        #drittes_oktett_binaer = (bin(int(netzIP[2])))
        #viertes_oktett_binaer = (bin(int(netzIP[3])))
        #print("Netzwerk binär: " + erstes_oktett_binaer + "." + zweites_oktett_binaer_final + "." + drittes_oktett_binaer_final + "." + viertes_oktett_binaer_final)
        # ich brauche min 2 IP-Adressen und kann dann vergleichen, in welchem Subnetz sie sein müssen?
        # Nullen zählen count()?
        # print(subnetzmaske)

        # Netzwerkadressen + Broadcastadressen
        for i in range(0, int(anz_subnetz)):
            print(str(i+1) + ". Subnetz:")
            print("Netzwerkadresse: " + str(netzIP[0]) + "." + str(netzIP[1]) + "." + str(netzIP[2]) + "." + str(int(netzIP[3]) + i * host_anz_subnetz))
            print("Broadcastadresse: " + str(netzIP[0]) + "." + str(netzIP[1]) + "." + str(netzIP[2]) + "." + str((int(netzIP[3]) + (i +1) * host_anz_subnetz) - 1))
            print()

        # Erneute Berechnung Ja/Nein
        erneute_berechnung = input("Erneute Berechnung erwünscht? (Ja/Nein): ")
        if erneute_berechnung == "Ja":
            wiederholen = True
        elif erneute_berechnung == "Nein":
            wiederholen = False


