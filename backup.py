import math
import re


# Basisnetz-Adresse: Eingabe und Prüfung (es darf kein Text eingegeben werden.)
def input_basisnetz_adresse():
    validEntry = False
    while(validEntry == False):
        netzadresse_basisnetz = input("Bitte gib die Basisnetz-Adresse ein (x.x.x.x): ")
        netzadresse_basisnetz_ohne_Punkte = netzadresse_basisnetz.replace(".", "")
        if netzadresse_basisnetz_ohne_Punkte.isdigit():
            validEntry = True
        else:
            print("Fehlerhafte Eingabe")
    netz_ip = netzadresse_basisnetz.split(".")
    return netz_ip

# Anzahl der Subnetzmaske: Eingabe und Prüfung (es darf kein Text eingegeben werden.)
def input_anzahl_subnetzmasken():
    validEntry = False
    while (validEntry == False):
        anz_subnetz = input("Wie viele Subnetze sind gewünscht?: ")
        if anz_subnetz.isdigit():                 # Prüfung, ob int
            validEntry = True
        else:
            print("Fehlerhafte Eingabe")
    anz_subnetz_as_int = int(anz_subnetz)
    return anz_subnetz_as_int

# Berechnung Subnetzmaske: (selbst berechnen)
def berechnung_subnetzmaske(log_anz_subnetz):
    subnetzmaske = 0
    for i in range(0, log_anz_subnetz):
        subnetzmaske = subnetzmaske + (1<<(7-i))
    return str(subnetzmaske)


# Wie viele Bits vom Host-Part müssen wir für den Netzwerkbereich klauen?
def berechnung_bits_aus_host_bereich(anz_subnetz_as_int):
    log_anz_subnetz = math.log2(anz_subnetz_as_int)
    return log_anz_subnetz


 # Wie viele Subnetze müssen erstellt werden?
def berechnung_anzahl_der_subnetze(log_anz_subnetz):
    if (log_anz_subnetz % 1) != 0:
        return int(log_anz_subnetz) + 1
    else:
        return int(log_anz_subnetz)


def ausgabe_anzahl_der_subnetze(log_anz_subnetz):
    print("Subnetzmaske: 255.255.255." + berechnung_subnetzmaske(log_anz_subnetz))
    print()


 # Berechnung Anzahl der möglichen Hosts pro Subnetz
def berechnung_anzahl_der_hosts(log_anz_subnetz):
    host_anz_subnetz = pow(2, 8 - log_anz_subnetz)
    anz_hosts = host_anz_subnetz - 2
    return anz_hosts

def ausgabe_anzahl_der_hosts(anz_hosts):
    print()
    print("Anzahl der Hosts im jeweiligen Subnetz: " + str(anz_hosts))



# Netzwerkadressen + Broadcastadressen
def ausgabe_netzwerk_broadcast_adressen(netz_ip, anz_subnetz_as_int, host_anz_subnetz):
    for i in range(0, anz_subnetz_as_int):
        print(str(i+1) + ". Subnetz:")
        print("Netzwerkadresse: " + str(netz_ip[0]) + "." + str(netz_ip[1]) + "." + str(netz_ip[2]) + "." + str(int(netz_ip[3]) + i * host_anz_subnetz))
        print("Broadcastadresse: " + str(netz_ip[0]) + "." + str(netz_ip[1]) + "." + str(netz_ip[2]) + "." + str((int(netz_ip[3]) + (i +1) * host_anz_subnetz) - 1))
        print()

# Erneute Berechnung Ja/Nein
def erneute_berechnung_abfrage():
    erneute_berechnung = input("Erneute Berechnung erwünscht? (Ja/Nein): ")
    if erneute_berechnung == "Ja":
        return True
    elif erneute_berechnung == "Nein":
        return False

# Fehlermeldung bei z.B. zu vielen Netzen soll ausgegeben werden (128 subnetze (dafür keine Hosts), 64 subnetze (2 hosts))
        #
        #
        #
        #


# ----------------------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    wiederholen = True

    while (wiederholen == True):
        netz_ip = input_basisnetz_adresse()
        anz_subnetz_as_int = input_anzahl_subnetzmasken()
        log_anz_subnetz = berechnung_bits_aus_host_bereich(anz_subnetz_as_int)
        subnetzmask = berechnung_subnetzmaske(log_anz_subnetz)
        anz_subnetz = berechnung_anzahl_der_subnetze(log_anz_subnetz)
        anz_hosts = berechnung_anzahl_der_hosts(log_anz_subnetz)
        ausgabe_netzwerk_broadcast_adressen(netz_ip, anz_subnetz, anz_hosts +2)
        wiederholen = erneute_berechnung_abfrage()



        # evtl. später bei flexibler Anwendung nötig:
        # actual_number_of_subnets = math.ceil(log_number_of_subnets)     # Aufrunden von anzahl_subnetz
        # print(actual_number_of_subnets)

        # evtl. später bei flexibler Subnetzmaske:
        #erstes_oktett_binaer = (bin(int(netzIP[0])))
        #zweites_oktett_binaer = (bin(int(netzIP[1])))
        #drittes_oktett_binaer = (bin(int(netzIP[2])))
        #viertes_oktett_binaer = (bin(int(netzIP[3])))
        #print("Netzwerk binär: " + erstes_oktett_binaer + "." + zweites_oktett_binaer_final + "." + drittes_oktett_binaer_final + "." + viertes_oktett_binaer_final)
        # ich brauche min 2 IP-Adressen und kann dann vergleichen, in welchem Subnetz sie sein müssen?
        # Nullen zählen count()?
        # print(subnetzmaske)