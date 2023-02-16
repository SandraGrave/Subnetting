class calculator:

    def __init__(self):
        print("dies ist ein Test")

    def calculate(self):
        wiederholen = True

        while (wiederholen == True):
            netzwerkAdresseBasisnetz = input("Wie lautet die Netzwerk-Adresse vom Basisnetz?: ")
            AnzSubnetz = input("Was ist die Anzahl der Subnetze?: ")
            NetzIP = netzwerkAdresseBasisnetz.split(".")    # Zerlegt Netzadresse in Array NetzIP
            print(NetzIP)

            """LogAnzSubnetz = log2(AnzSubnetz)

                if (LogAnzSubnetz % 1) == 0:
                    continue
                else:
                    LogAnzSubnetz = int(LogAnzSubnetz) + 1

        HostAnzSubnetz = 2 ^ (8 - LogAnzSubnetz)
        print(HostAnzSubnetz)  # A: Anzahl der möglichen Hosts pro Netz HostAnzSubnetz-2
        # A: Subnetzmaske für die Netze: ??? (selbst berechnen)

            for i in range(0, HostAnzSubnetz):      # i = 0; i < AnzSubnetze; i++
                print(i)      # A: Netz i : NetzIP[0] + NetzIP[1] + NetzIP[2] + NetzIP[3] + i * HostAnzSubnetz)

        # erneute Berechnung? Eingabe
        # Eingabe Ja : Wiederholen =True
        # Eingabe Nein: Wiederholen = False"""