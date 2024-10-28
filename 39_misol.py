"""A va B butun soni berilgan. (A < B). A va B sonlari orasidagi barcha butun sonlarni chiqaruvchi programma tuzilsin.
Bunda har bir son o'zining qiymaticha chiqarilsin. Ya'ni 3 soni 3 marta chiqarilsin. """

A = int(input("A sonini kiriting: "))
B = int(input("B sonini kiriting: "))

if (A < B):
    for x in range (A, B + 1):
        for i in range(A, x + 1):
            print(x)
else: 
    print(f"{A} < {B} ? {B} katta bo'lishi kerak {A} dan")