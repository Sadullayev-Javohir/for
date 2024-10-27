"""n butun soni berilgan (n > 0). Shu sonning kvadratini quyidagi formula asosida hisoblovchi programma tuzilsin.
"""

n = int(input("n sonini kiriting: "))

total = 0

if (n > 0):
    for x in range(n):
        total = total + (2 * x + 1)
    print(total)
else:
    print(f"{n} > 0 ? {n} katta bo'lishi kerak 0 dan")