"""k va n butun sonlari berilgan. (n > 0). k sonini n marta chiqaruvchi programma tuzilsin."""

k = int(input("k sonini kiriting: "))
n = int(input("n sonini kiriting: "))

if (n > 0):
    for _ in range(n):
        print(k)
else:
    print(f"{n} > 0 ? {n} katta bo'lishi kerak")