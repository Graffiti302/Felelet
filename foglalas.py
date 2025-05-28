print("Üdvözlünk a mozi szék foglaló programban!")
print("Választhatsz egy sor székből a moziteremben!")
székek = [1, 2, 3, 4, 6, 7, 8]

def Valami():
    Valasztas = int(input("Melyik széket választod?[1-8]:"))
    if 1 < Valasztas > 8:
        print("Ez nem opció")
        Valami()
    if Valasztas == 5:
        print("Ez sajnos nem foglalható. Oszlop van a helyén!")
        Valami()
    if Valasztas == 1 or 2 or 3 or 4 or 6 or 7 or 8:
        Veglegesites =  str(input(f"Biztos hogy ezt a helyet akarod Y/N:({Valasztas})"))
        if Veglegesites == "N":
            print("Akkor válassz másikat!")
            Valami()
        if Veglegesites == "Y":
            print(f"Köszonjük a vásárlásrt! Az ön széke a/az: {Valasztas}.")
        
            szabad = [1,2,3,4,5,6,7,8]
            Valasztas-1
            szabad.remove(Valasztas)
            szabad.append("📗")
            for i in range (1):
                print(szabad)

    if 1 < Valasztas > 8:
        print("Ez nem opció")
        Valami()
Valami()


