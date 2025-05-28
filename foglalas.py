print("Üdvözlünk a mozi szék foglaló programban!")
print("Választhatsz egy sor székből a moziteremben!")
székek = [1, 2, 3, 4, 5, 6, 7, 8]
Valasztas = int(input("Melyik széket választod?[1-8]:"))

if Valasztas != 1 or 2 or 3 or 4 or 6 or 7 or 8:
    
    print("Ez nem opció")
elif Valasztas == 5:
    print("Ez sajnos nem foglalható. Oszlop van a helyén!")
else:
    print(f"Köszonjük a vásárlásrt! Az ön széke a/az: {Valasztas}.")
#szünet

