wiederholen = True

while (wiederholen == True):
    netzwerkAdresseBasisnetz =
    AnzSubnetz =                    # Anzahl der gewünschten Subnetze
    # Zerlege Netzadresse in Array NetzIP
    # LogAnzSubnetz = log2(AnzSubnetz)

        if (LogAnzSubnetz mod 1) == 0:
            continue
        else: LogAnzSubnetz = int(LogAnzSubnetz)+1

    HostAnzSubnetz = 2^(8-LogAnzSubnetz)
    # A: Anzahl der möglichen Hosts pro Netz HostAnzSubnetz-2
    # A: Subnetzmaske für die Netze: ??? (selbst berechnen)

    for i = 0; i < AnzSubnetze; i++:
        # A: Netz i : NetzIP[0] + NetzIP[1] + NetzIP[2] + NetzIP[3] + i * HostAnzSubnetz)

    # erneute Berechnung? Eingabe
    # Eingabe Ja : Wiederholen =True
    # Eingabe Nein: Wiederholen = False
