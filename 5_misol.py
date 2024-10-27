"""Bir kg konfetning narxi berilgan (haqiqiy son). 0.1, 0.2, 0.3 ... 1 kg konfetning narxini chiqaruvchi programma tuzilsin. """

narx = float(input("Konfet narxini kiriting: "))

for x in range(1, 11):
    weight = x / 10
    
    print(f"{weight} kg konfet narxi: {weight * narx}")