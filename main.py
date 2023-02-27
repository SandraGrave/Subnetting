import math
import re


# Basisnetz-Adresse: Eingabe und Prüfung (es darf kein Text eingegeben werden.)
def eingabe_basisnetz():
    validEntry = False
    while (validEntry == False):
        netzadresse_basisnetz = input("Bitte gib die Basisnetz-Adresse ein (x.x.x.x): ")
        netzadresse_basisnetz_ohne_Punkte = netzadresse_basisnetz.replace(".", "")
        if netzadresse_basisnetz_ohne_Punkte.isdigit():
            validEntry = True
        else:
            print("Fehlerhafte Eingabe")
    return netzadresse_basisnetz


# Anzahl der Subnetzmaske: Eingabe und Prüfung (es darf kein Text eingegeben werden und nicht zu HOhe Anzahl der Subnetze)
# Fehlermeldung bei z.B. zu vielen Netzen soll ausgegeben werden (128 subnetze (dafür keine Hosts, macht keinen Sinn), 64 subnetze (2 hosts))
def eingabe_anz_subnetzmaske():
    validEntry = False
    while (validEntry == False):
        anz_subnetz = input("Wie viele Subnetze sind gewünscht?: ")
        if anz_subnetz.isdigit():  # Prüfung, ob int
            if int(anz_subnetz) > 64:
                print("Bei so vielen Subnetzen können keine Host-Adressen mehr vergeben werden. Bitte gib eine geringere Subnetz-Anzahl an")
            else: validEntry = True
        else:
            print("Fehlerhafte Eingabe")
    return int(anz_subnetz)



def teile_netzip_als_array(netzadresse_basisnetz):
    return netzadresse_basisnetz.split(".")


# Wie viele Bits vom Host-Part müssen wir für den Netzwerkbereich klauen, um die SUbnetze erstellen zu können?
def berechne_bits_aus_hostpart(anz_subnetz_as_int):
    return math.log2(anz_subnetz_as_int)


# Wie viele Subnetze müssen erstellt werden?
def berechnung_anz_subnetze(log_anz_subnetz):
    if (log_anz_subnetz % 1) != 0:
        return int(log_anz_subnetz) + 1
    else:
        return int(log_anz_subnetz)


# Berechnung Anzahl der möglichen Hosts pro Subnetz
def berechnung_anz_host(log_anz_subnetz):
    host_anz_subnetz = pow(2, 8 - log_anz_subnetz)
    return host_anz_subnetz - 2


def ausgabe_anz_host(anz_hosts):
    print("\n" + "Anzahl der Hosts im jeweiligen Subnetz: " + str(anz_hosts))



# Berechnung Subnetzmaske: (selbst berechnen)
def berechnung_subnetzmaske(log_anz_subnetz):
    subnetzmaske = 0
    for i in range(0, log_anz_subnetz):
        subnetzmaske = subnetzmaske + (1<<(7-i))
    return str(subnetzmaske)

def ausgabe_subnetzmaske(log_anz_subnetz):
    print("Subnetzmaske: 255.255.255." + berechnung_subnetzmaske(log_anz_subnetz))
    print()


def ausgabe_netzwerk_broadcast(anz_subnetz, netzIP, host_anz_subnetz):
    for i in range(0, int(anz_subnetz)):
        print(str(i + 1) + ". Subnetz:")
        print("Netzwerkadresse: " + str(netzIP[0]) + "." + str(netzIP[1]) + "." + str(netzIP[2]) + "." + str(
            int(netzIP[3]) + i * host_anz_subnetz))
        print("Broadcastadresse: " + str(netzIP[0]) + "." + str(netzIP[1]) + "." + str(netzIP[2]) + "." + str(
            (int(netzIP[3]) + (i + 1) * host_anz_subnetz) - 1))
        print()

def erneute_berechnung_abfrage():
    erneute_berechnung = input("Erneute Berechnung erwünscht? (Ja/Nein): ")
    if erneute_berechnung == "Ja":
        return True
    elif erneute_berechnung == "Nein":
        return False





if __name__ == '__main__':
    wiederholen = True

    while (wiederholen == True):

        netzadresse_basisnetz = eingabe_basisnetz()
        anz_subnetz = eingabe_anz_subnetzmaske()
        netzIP = teile_netzip_als_array(netzadresse_basisnetz)
        log_anz_subnetz = berechne_bits_aus_hostpart(anz_subnetz)
        log_anz_subnetz = berechnung_anz_subnetze(log_anz_subnetz)
        anz_hosts = berechnung_anz_host(log_anz_subnetz)
        ausgabe_anz_host(anz_hosts)
        ausgabe_subnetzmaske(log_anz_subnetz)
        ausgabe_netzwerk_broadcast(anz_subnetz, netzIP, anz_hosts + 2)
        wiederholen = erneute_berechnung_abfrage()


# später?
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
        # print(subnetzmaske