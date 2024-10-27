"""a va b butun sonlari berilgan. (a < b). a va b sonlari orasidagi barcha butun sonlarni (a va b ni ham) chiqaruvchi
va chiqarilgan sonlar sonini chiqaruvchi programma tuzilsin. (a va b xam chiqarilsin.)"""

a = int(input("Son kiriting: "))
b = int(input("Son kiriting: "))

if (a < b):
    for x in range(a, b + 1):
        print(x)
    print("Chiqarilgan sonlar soni: ", b - a + 1)
else: 
    print(f"{a} < {b} ? {b} katta bo'lishi kerak")