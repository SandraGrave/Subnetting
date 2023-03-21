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


def eingabe_der_subnetz_maske():  # min 8, max 30
    eingegebener_wert = validiere_zahl_zwischen(8, 29, "Du brauchst mindestens einen Präfix von 8",
                                                "Bei über 29 Subnetzen können keine Hosts mehr vergeben werden, bitte gib eine geringe Anzahl an",
                                                "Wie viele Bits sind als Netzwerkpart gewünscht? (min 8, max 29): ")
    return 32-eingegebener_wert


# Anzahl der Subnetzmaske: Eingabe und Prüfung (es darf kein Text eingegeben werden und nicht zu HOhe Anzahl der Subnetze)
# Fehlermeldung bei z.B. zu vielen Netzen soll ausgegeben werden (128 subnetze (dafür keine Hosts, macht keinen Sinn), 64 subnetze (2 hosts))
def eingabe_anz_subnetzmaske(freie_subnetz_stellen):    # negative Zahlen Fehlermeldung fehlt noch
    eingegebener_wert = validiere_zahl_zwischen(2, pow(2, (freie_subnetz_stellen)), "Bitte gib keine Zahl unter 2 oder negativen Zahlen ein",
                                                "Bei so vielen Subnetzen können keine Host-Adressen mehr vergeben werden. Bitte gib eine geringere Subnetz-Anzahl an, das Maximum an möglichen Netzen ist: " + str(pow(2, (freie_subnetz_stellen))),
                                                "Wie viele Subnetze sind gewünscht? (min 2, max " + str(pow(2, (freie_subnetz_stellen))) + "): ")

    return eingegebener_wert


def validiere_zahl_zwischen(min, max, fehler_min, fehler_max, frage):
    validEntry = False
    while (validEntry == False):
        subnetzmaske = input(frage)
        if subnetzmaske.isdigit():
            if int(subnetzmaske) < min:
                print(fehler_min)
            elif int(subnetzmaske) > max:
                print(fehler_max)
            else:
                validEntry = True
        else:
            print("Fehlerhafte Eingabe")
    return int(subnetzmaske)

def teile_netzip_als_array(netzadresse_basisnetz):
    return netzadresse_basisnetz.split(".")


# Wie viele Bits vom Host-Part müssen wir für den Netzwerkbereich klauen, um die Subnetze erstellen zu können?
def berechne_bits_aus_hostpart(anz_subnetz_as_int):
    return math.log2(anz_subnetz_as_int)


# Wie viele Subnetze müssen erstellt werden?
def berechnung_anz_subnetze(anz_bits_subnetzpart):
    if (anz_bits_subnetzpart % 1) != 0:
        return int(anz_bits_subnetzpart) + 1
    else:
        return int(anz_bits_subnetzpart)


# Berechnung Anzahl der möglichen Hosts pro Subnetz
def berechnung_anz_host(log_anz_subnetz, anz_bits_subnetz):
    host_anz_subnetz = pow(2, anz_bits_subnetz - log_anz_subnetz)
    return host_anz_subnetz - 2


def ausgabe_anz_host(anz_hosts):
    print("\nAnzahl der Hosts pro Subnetz: " + str(anz_hosts))



def berechnung_subnetzmaske(log_anz_subnetz, freie_bits_hostpart):
    subnetzmaske = 0
    for i in range(0, 32 - freie_bits_hostpart):   # 32 Bits - erstes Oktett = 24
        subnetzmaske = subnetzmaske + (1 << (32-i-1))
    for i in range(0, log_anz_subnetz):
        subnetzmaske = subnetzmaske + (1 << (freie_bits_hostpart - i - 1))         # da wir das erste Bit schon festgelegt haben, müssen wir 1 abziehen. Da wir bei 0 anfangen zu zählen
    return subnetzmaske


def umwandlung_int_32_zu_subnetzmaske(subnetzmaske):                    #weil 32 bits, um eine Zahl darzustellen
    subnetz_maske_as_string = str((subnetzmaske & 0b11111111000000000000000000000000) >> 24) + "." + str((subnetzmaske & 0b111111110000000000000000) >> 16) + "." + str((subnetzmaske & 0b1111111100000000) >> 8) + "." + str((subnetzmaske & 0b11111111))
    return subnetz_maske_as_string


def ausgabe_subnetzmaske(subnetzmaske_as_string):
    print("Subnetzmaske: " + subnetzmaske_as_string + "\n")


def umwandlung_subnetzmaske_zu_int_32(netz_ip):  # netz_ip wird in 32er-Bit-Int umgewandelt
    int_first_part = int(netz_ip[0]) << 24                                   # 11111111000000000000000000000000
    int_second_part = int(netz_ip[1]) << 16                                  # 00000000111111110000000000000000
    int_third_part = int(netz_ip[2]) << 8                                    # 00000000000000001111111100000000
    int_forth_part = int(netz_ip[3])                                         # 00000000000000000000000011111111
    netz_ip_as_int = int_first_part + int_second_part + int_third_part + int_forth_part
    return netz_ip_as_int


def berechnung_netzwerk_adresse(aktueller_durchlauf, netz_ip_netzwerkteil, beginn_host_part):
    temp_netzwerkadresse = netz_ip_netzwerkteil + (aktueller_durchlauf << (beginn_host_part - (math.ceil(berechne_bits_aus_hostpart(anz_subnetz)))))
    netzwerkadresse = str((temp_netzwerkadresse & 0b11111111000000000000000000000000) >> 24) + "." + str(
        (temp_netzwerkadresse & 0b111111110000000000000000) >> 16) + "." + str(
        (temp_netzwerkadresse & 0b1111111100000000) >> 8) + "." + str((temp_netzwerkadresse & 0b11111111))
    return netzwerkadresse

def berechnung_broadcast_adresse(aktueller_durchlauf, netz_ip_netzwerkteil, beginn_host_part):
    temp_broadcastadresse = netz_ip_netzwerkteil + ((aktueller_durchlauf + 1) << (beginn_host_part - (math.ceil(berechne_bits_aus_hostpart(anz_subnetz))))) - 1
    broadcastadresse = str((temp_broadcastadresse & 0b11111111000000000000000000000000) >> 24) + "." + str(
        (temp_broadcastadresse & 0b111111110000000000000000) >> 16) + "." + str(
        (temp_broadcastadresse & 0b1111111100000000) >> 8) + "." + str((temp_broadcastadresse & 0b11111111))
    return broadcastadresse

def erstelle_bitmaske_netzwerkpart(freie_bits_hostpart):  # Anzahl der Bits für Netzwerkpart, 1en werden gesetzt
    bitmaske_netzwerkpart = 0
    for i in range(0, 32-(int(freie_bits_hostpart))):
        bitmaske_netzwerkpart = bitmaske_netzwerkpart + (1 << (31 - i))
    return bitmaske_netzwerkpart

def berechnung_netzwerk_broadcast(anz_subnetz, netz_ip_as_int, freie_bits_hostpart):
    beginn_host_part = int(freie_bits_hostpart)
    netzwerkadressen_liste = []
    broadcastadressen_liste = []

    bitmaske_netzwerkpart = erstelle_bitmaske_netzwerkpart(freie_bits_hostpart)
    netz_ip_netzwerkteil = netz_ip_as_int & bitmaske_netzwerkpart            # & bitwise and, Netzwerkpart, wo überlappen sich die 1en

    for aktueller_durchlauf in range(0, anz_subnetz):                        #
        netzwerkadresse = berechnung_netzwerk_adresse(aktueller_durchlauf, netz_ip_netzwerkteil, beginn_host_part)
        netzwerkadressen_liste.append(netzwerkadresse)
        broadcastadresse = berechnung_broadcast_adresse(aktueller_durchlauf, netz_ip_netzwerkteil, beginn_host_part)
        broadcastadressen_liste.append(broadcastadresse)
    return [netzwerkadressen_liste, broadcastadressen_liste]


def ausgabe_netzwerk_broadcast(netzwerkadressen_liste):
    elements = len(netzwerkadressen_liste[0])

    for i in range(0, elements):
        print(str(i + 1) + ". Subnetz:")
        print("Netzwerkadresse: " + netzwerkadressen_liste[0][i])
        print("Broadcastadresse: " + netzwerkadressen_liste[1][i] + "\n")

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
        freie_bits_hostpart = eingabe_der_subnetz_maske()
        anz_subnetz = eingabe_anz_subnetzmaske(freie_bits_hostpart)
        netz_ip = teile_netzip_als_array(netzadresse_basisnetz)
        anz_bits_host_part = berechne_bits_aus_hostpart(anz_subnetz)
        anz_bits_subnetzpart = berechnung_anz_subnetze(anz_bits_host_part)
        anz_hosts = berechnung_anz_host(anz_bits_subnetzpart, freie_bits_hostpart)
        ausgabe_anz_host(anz_hosts)
        netz_ip_as_int = umwandlung_subnetzmaske_zu_int_32(netz_ip)
        netzwerkadressen_liste = berechnung_netzwerk_broadcast(anz_subnetz, netz_ip_as_int, freie_bits_hostpart)
        subnetzmaske = berechnung_subnetzmaske(anz_bits_subnetzpart, freie_bits_hostpart)
        subnetzmaske_as_string = umwandlung_int_32_zu_subnetzmaske(subnetzmaske)
        ausgabe_subnetzmaske(subnetzmaske_as_string)
        ausgabe_netzwerk_broadcast(netzwerkadressen_liste)
        wiederholen = erneute_berechnung_abfrage()