"""n butun soni va a haqiqiy soni berilgan (n > 0). a ning n - darajasini aniqlovchi programma tuzilsin.
"""

a = int(input("a sonini kiriting: "))
n = int(input("n sonini kiriting: "))

S = 0

if (n > 0):
    for x in range(a, n + 1):
        S = a ** n
    print(S)
else:
    print(f"{n} > 0 ? {n} katta bo'lishi kerak 0 dan")