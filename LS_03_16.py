#Задача 16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
array = {}
for i in range(int(input('Число N: '))):
    k = int(input('Число A'+str(i)+': '))
    if k in array:
        array[k] = array[k]+1
    else:
        array[k] = 1
x = int(input('Число X: '))    
if x in array:
    print(array[x])
else:
    print(0)    
