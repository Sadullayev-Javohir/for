"""n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma tuzilsin. 
S = n ** 2 + (n + 1)**2 + (n + 2)**2 + ... (2 * n)**2"""

n = int(input("n sonini kiriting: "))

S = 0

if (n > 0):
    for x in range(1, n + 1):
        S += n ** 2 + (n + n) ** 2    
    print(S)
else:
    print(f"{n} > 0 {n} katta bo'lishi kerak 0 dan")
    