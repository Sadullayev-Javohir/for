"""Bir kg konfetning narxi berilgan (haqiqiy son). 1, 2, ..., 10 kg konfetning narxini chiqaruvchi programma tuzilsin. """
narx = float(input("Konfetning narxini kiriting: "))

for x in range(1, 11):
    print(x, "kg konfetning narxi: ", x * narx)