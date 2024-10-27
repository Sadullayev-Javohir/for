"""n butun soni va a haqiqiy soni berilgan. (n > 0). Bir sikldan foydalanib a ning 1 dan n gacha bo'lgan
barcha darajalarini chiqaruvchi programma tuzilsin."""

a = int(input("a sonini kiriting: "))
n = int(input("n sonini kiriting: "))

daraja = 0

if (n > 0):
    for x in range(1, n + 1, 1):
        daraja = a ** x
        print(f"{a} ** {x} = {daraja}")
else: 
    print("n soni 0 dan katta bo'lishi kerak")