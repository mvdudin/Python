#Задача 18
# Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

array = []
for i in range(int(input('Число N: '))):
    array.append(int(input('Число A'+str(i)+': ')))
x = int(input('Число X: '))
k = 0
for i in range(1, len(array)):
    if abs(array[i]-x) < abs(array[k]-x):
        k=i
print(array[k])
