print("Üdvözlünk a mozi szék foglaló programban!")
print("Választhatsz egy sor székből a moziteremben!")
székek = [1, 2, 3, 4, 5, 6, 7, 8]
Valasztas = int(input("Melyik széket választod?[1-8]:"))

if 1 < Valasztas > 8:
    print("Ez nem opció")
else:
    print(f"Köszonjük a vásárlásrt! Az ön széke a/az: {Valasztas}.")

for i in range (8):
    print()