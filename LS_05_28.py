# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def RecursionSum(a, b):
    if a > 0 and b > 0: 
        return RecursionSum(a-1, b-1)+1+1
    elif a > 0:     
        return RecursionSum(a-1, 0)+1
    elif b > 0:    
        return RecursionSum(0, b-1)+1
    else:
        return 0
print(RecursionSum(9, 5))