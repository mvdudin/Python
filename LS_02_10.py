#Задача 10: 
#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть

o = 0
r = 0
for i in range(int(input('Количество монет на столе: '))):
    m = 2
    while m != 0 and m != 1:
        m = int(input('Орел 1 или решка 0: '))
    if m:
        o += 1
    else:
        r += 1
if o < r :
    r = o
print('Надо перевернуть ',r , 'монет')