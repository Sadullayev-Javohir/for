"""a va b butun sonlari berilgan. (a < b). a va b sonlari orasidagi barcha butun sonlarni (a va b dan tashqari) 
kamayish tartibida chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi programma tuzilsin."""

a = int(input("a sonini kiriting: "))
b = int(input("b sonini kiriting: "))

if (a < b):
    for x in range(b - 1, a, -1):
        print(x)        
    print("Chiqarilgan sonlar soni: ", b - a - 1)
else:
    print(f"{a} < {b} ? {b} katta bo'lishi kerak")