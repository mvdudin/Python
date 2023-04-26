# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

indexs = []
min_value = 5
max_value = 15
values = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

for i in range(len(values)):
    if  min_value < values[i] and values[i] < max_value:
        indexs.append(i)
print(indexs)


