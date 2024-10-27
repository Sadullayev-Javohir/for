"""n butun soni berilgan (n > 0). Quyidagi ko'paytmani hisoblovchi programma tuzilsin. S = 1.1 * 1.2 * 1.3 * ..."""

n = int(input("n sonini kiriting: "))

S = 1

if (n > 0):
    for x in range(1, n + 1):
        divide = x / 10
        S *= divide
        print(S)
else:
    print(f"{n} > 0 ? {n} katta bo'lishi kerak 0 dan")