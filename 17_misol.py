"""n butun soni va a haqiqiy soni berilgan. (n > 0). Bir sikldan foydalanib a ning 1 dan n gacha bo'lgan
barcha darajalarni chiqaruvchi va yig'indisini hisoblovchi programma tuzilsin."""

a = int(input("a sonini kiriting: "))
n = int(input("n sonini kiriting: "))

daraja = 0

if (n > 0):
    for x in range(1, n + 1):
        daraja += a ** x
    print(daraja)
else: 
    print(f"{n} > 0 ? {n} katta bo'lishi kerak 0 dan")