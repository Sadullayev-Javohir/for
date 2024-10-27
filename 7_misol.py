"""a va b butun sonlari berilgan (a < b). a dan b gacha bo'lgan barcha butun sonlar yig'indisini chiqaruvchi
programma tuzilsin."""

a = int(input("a sonini kiriting: "))
b = int(input("b sonini kiriting: "))

total = 0

if (a < b):
    for x in range(a, b + 1):
    
        total = total + x
    
    print(total)

else:
    print(f"{a} < {b} ? {b} katta bo'lishi kerak")
