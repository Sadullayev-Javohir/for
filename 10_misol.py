"""n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma tuzilsin."""

n = int(input("n sonini kiriting: "))

S = 0
one = 1

if (n > 0):
    for x in range(1, n + 1):
        S += 1 + one / x 
    print(S)
else: 
    print(f"{n} > 0 ? {n} katta bo'lishi kerak 0 dan")