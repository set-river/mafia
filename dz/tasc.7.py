#Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
#Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
a = list(range(1000))
y = len(a)
for i in range(y+1):
    if i % 3 == 0:
        pass
    elif i % 5 == 0:
        pass
    else:
        a.remove(i)
print(a)