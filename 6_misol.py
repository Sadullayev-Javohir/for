"""Bir kg konfetning narxi berilgan. 1.2, 1.4 ..., 2 kg konfetning narxini chiqaruvchi programma tuzilsin."""

narx = float(input("Konfet narxini kiriting: "))

for x in range(12, 22, 2):
    weight = x / 10
    print(f"{weight} kg konfetning narxi: {weight * narx}")