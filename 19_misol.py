"""n butun soni berilgan (n > 0). Birdan n gacha bo'lgan sonlar ko'paytmasini chiqaruvchi programma tuzilsin.
n! = 1 * 2 * ... n"""

n = int(input("n sonini kiriting: "))
factorial = 1

if (n > 0):
    for x in range(1, n + 1):
        factorial *= x
    print(factorial)
else:
    print(f"{n} > 0 ? {n} katta bo'lishi kerak 0 dan")