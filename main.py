import math
import re

if __name__ == '__main__':
    wiederholen = True

    while (wiederholen == True):
        #netzadresse_basisnetz = input("Bitte gib die Basisnetz-Adresse ein (x.x.x.x): ")
        anz_subnetz = input("Wie viele Subnetze sind gewünscht?: ")

        # Basisnetz-Adresse: Eingabe und Prüfung (es darf kein Text eingegeben werden.)
        validEntry = False
        while(validEntry == False):
            netzadresse_basisnetz = input("Bitte gib die Basisnetz-Adresse ein (x.x.x.x): ")
            netzadresse_basisnetz_ohne_Punkte = netzadresse_basisnetz.replace(".", "")
            if netzadresse_basisnetz_ohne_Punkte.isdigit():
                validEntry = True
            else:
                print("Fehlerhafte Eingabe")

        # Fehlermeldung bei z.B. zu vielen Netzen soll ausgegeben werden (128 subnetze (dafür keine Hosts), 64 subnetze (2 hosts))
        # Prüfung, ob Zahl eingegeben wurde, Fehlermeldung

        anz_subnetz_as_int = int(anz_subnetz)
        netzIP = netzadresse_basisnetz.split(".")
        log_anz_subnetz = math.log2(anz_subnetz_as_int)

        # actual_number_of_subnets = math.ceil(log_number_of_subnets)     # Aufrunden von anzahl_subnetz
        # print(actual_number_of_subnets)

        if (log_anz_subnetz % 1) != 0:
            log_anz_subnetz = int(log_anz_subnetz) + 1
        else:
            log_anz_subnetz = int(log_anz_subnetz)

        host_anz_subnetz = pow(2, 8 - log_anz_subnetz)
        print(host_anz_subnetz)
        anz_hosts = host_anz_subnetz - 2
        print("Anzahl der Hosts im jeweiligen Subnetz: " + str(anz_hosts))

        # A: Subnetzmaske für die Netze: ??? (selbst berechnen)
        # print( Subnetzmaske)

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



