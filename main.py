# Výpočet BMI:
# vstup: výška v m (desetinné), váha v kg (celočíselné)
# BMI je rovno podílu váhy a druhé mocniny výšky
# Program vypíše výsledek (číselně) a zároveň slovy:
# bmi < 18.5 "podváha"
# 18.5 .. 25 "normální"
# 25 .. 30 "nadváha"
# 30 < bmi "obezita"
#
# Trojúhelníky:
# vstup: strany a, b, c (desetinné nebo celočíselné)
# Výstup: program vyhodnotí, zda se jedná o trojúhelník
# a) rovnoramenný
# b) rovnostranný
# c) pravoúhlý (je třeba nalézt přeponu)
# Pokud ze zadaných rozměrů trojúhelník sestrojit nelze, program to vypíše a nic vyhodnocovat nebude.
# Program může umožnit nové zadání údajů bez nutnosti program znovu spouštět.
#
# Datum narození:
# vstup: datum narození ve formátu DD.MM.RRRR
# Program zjistí, zda se jedná o platné datum.
# Počet dnů od 1 do 31 (kdo zvládne, může řešit i počty dnů v jednotlivých měsících).
# Počet měsíců od 1 do 12.
# Počet roků od 1 do 2021.
# Pokud délka vstupního řetězce nebude rovna 10, program vypíše chybu a skončí (nebo umožní zadat datum znovu).
# Najděte, jak lze v Pythonu odstranit mezery na začátku a konci řetězce.

import datetime

print("1. Výpočet BMI")
print("2. Identifikace trojúhelníku")
print("3. Ověření data narození")

volba=int(input("Vyberte vzorec: "))
match volba:
    case 1:
        vyska = float(input("Zadejte Vaší výšku v metrech: "))
        vaha = int(input("Zadejte Vaší váhu: "))
        bmi = float(vaha / vyska ** 2)
        if bmi < 18.5:
            print("Jste podvyživený, ", "Vaše BMI je: ", bmi)
        elif 18.5 < bmi < 25:
            print("Vaše BMI je normální, ", "Vaše BMI je: ", bmi)
        elif bmi > 30:
            print("Jste obézní, ", "Vaše BMI je: ", bmi)
    case 2:
        while 1 == 1:

            stranaA = float(input("Zadejte stranu A: "))
            stranaB = float(input("Zadejte stranu B: "))
            stranaC = float(input("Zadejte stranu C: "))

            stran = True
            rov = True
            prav = True

            # není trojúhelník
            if stranaA + stranaB < stranaC or stranaA + stranaC < stranaB or stranaB + stranaC < stranaA:
                print("Není trojúhelník")

            # pravoúhlý
            if stranaA > stranaB and stranaA > stranaC:
                if stranaB * stranaB + stranaC * stranaC == stranaA * stranaA:
                    print("Trojúhelnîk je pravoúhlý s přeponou A")
                    prav = False

            elif stranaB > stranaA and stranaB > stranaC:
                if stranaA * stranaA + stranaC * stranaC == stranaB * stranaB:
                    print("Trojúhelnîk je pravoúhlý s přeponou B")
                    prav = False

            elif stranaC > stranaA and stranaC > stranaB:
                if stranaA * stranaA + stranaB * stranaB == stranaC * stranaC:
                    print("Trojúhelnîk je pravoúhlý s přeponou C")
                    prav = False

            # rovnostranny
            if stranaC == stranaA and stranaC == stranaB and stranaB == stranaA:
                print("Trojúhelník je rovnostranný")
                rov = False

            # rovnoramenny
            if stranaC == stranaA:
                print("Trojúhelník je rovnoramenný")
                stran = False
            if stranaC == stranaB:
                print("Trojúhelník je rovnoramenný")
                stran = False
            if stranaB == stranaA:
                print("Trojúhelník je rovnoramenný")
                stran = False

            if (prav):
                if (rov):
                    if (stran):
                        print("Obecný trojúhelník")
            # Ukonceni programu
            konec = int(input("Zadej číslo 1 pro ukončení programu / pro pokračování zadej 0: "))
            if konec == 1:
                exit()

    case 3:
        datum = input("Zadejte datum narození ve tvaru dd/mm/rr: ")
        # Kontrola cifer
        cislo = (len(str(datum)))
        delka = cislo - 2
        if delka > 8:
            print("Zadali jste špatné datum")
            exit()
        # rozdeleni inputu
        day, month, year = datum.split('/')
        validDatum = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            validDatum = False
        if (validDatum):
            print("datum je platný")
        else:
            print("datum je neplatný")

