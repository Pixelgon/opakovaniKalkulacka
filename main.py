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

cycle = True

while cycle==True:
    print("1. Výpočet BMI")
    print("2. Identifikace trojúhelníku")
    print("3. Ověření data narození")
    print("4. Konec")

    volba=int(input("Vyberte možnost (číselně): "))
    match volba:
        case 1:
            vyska = float(input("Zadejte vaší výšku v metrech: "))
            vaha = int(input("Zadejte vaší váhu v kilogramech: "))
            bmi = float(vaha / vyska ** 2)
            if bmi < 18.5:
                print("     Jste podvyživený,", "Vaše BMI je: ", bmi)
            elif 18.5 < bmi < 25:
                print("     Vaše BMI je normální,", "Vaše BMI je: ", bmi)
            elif bmi > 30:
                print("     Jste obézní, ", "Vaše BMI je: ", bmi)
        case 2:
            cyclet = 1
            while cyclet == 1:
                exist = True
                stranaA = float(input("Zadejte stranu A v centimetrech: "))
                stranaB = float(input("Zadejte stranu B v centimetrech: "))
                stranaC = float(input("Zadejte stranu C v centimetrech: "))

                stran = True
                rov = True
                prav = True

                # není trojúhelník
                if stranaA + stranaB < stranaC or stranaA + stranaC < stranaB or stranaB + stranaC < stranaA:
                    print("     Není trojúhelník")
                    exist = False
                if exist == True:
                    # pravoúhlý
                    if stranaA > stranaB and stranaA > stranaC:
                        if stranaB * stranaB + stranaC * stranaC == stranaA * stranaA:
                            print("     Trojúhelnîk je pravoúhlý s přeponou A")
                            prav = False

                    elif stranaB > stranaA and stranaB > stranaC:
                        if stranaA * stranaA + stranaC * stranaC == stranaB * stranaB:
                            print("     Trojúhelnîk je pravoúhlý s přeponou B")
                            prav = False

                    elif stranaC > stranaA and stranaC > stranaB:
                        if stranaA * stranaA + stranaB * stranaB == stranaC * stranaC:
                            print("     Trojúhelnîk je pravoúhlý s přeponou C")
                            prav = False

                    # rovnostranny
                    if stranaC == stranaA and stranaC == stranaB and stranaB == stranaA:
                        print("     Trojúhelník je rovnostranný")
                        rov = False

                    # rovnoramenny
                    if stranaC == stranaA or  stranaC == stranaB or stranaB == stranaA:
                        print("     Trojúhelník je rovnoramenný")
                        stran = False

                    if (prav):
                        if (rov):
                            if (stran):
                                print("     Obecný trojúhelník")
                                cyclet = False
                print("Chcete nový výpočet?(Zadejte číselně)")
                print("     1. ANO")
                print("     2. NE")
                cyclet = int(input())
        case 3:
            cyclen = True
            while cyclen == True:
                datum = input("Zadejte datum narození ve tvaru dd/mm/rr: ")
                # Kontrola cifer
                cislo = (len(str(datum)))
                if cislo != 10:
                    print("Zadali jste špatně datum")
                else:
                    # rozdeleni inputu
                    day, month, year = datum.split('/')
                    validDatum = True
                    try:
                        datetime.datetime(int(year), int(month), int(day))
                    except ValueError:
                        validDatum = False
                    if (validDatum):
                        print("     Datum narození", datum, "je platný")
                        cyclen = False
                    else:
                        print("     Datum narození", datum, "je neplatný")
                        cyclen = False
        case 4:
            print("Bye")
            exit()
