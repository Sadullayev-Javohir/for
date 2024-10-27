"""n butun soni berilgan (n > 0). Bir sikldan foydalangan holda quyidagi yig'indini hisoblovchi programma 
tuzilsin."""

n = int(input("n sonini kiriting: "))

factorial = 1
add = 0
if (n > 0):
    for x in range(1, n + 1):
        factorial *= x
        add += factorial
    print(add)
else:
    print(f"{n} > 0 ? {n} katta bo'lishi kerak 0 dan")