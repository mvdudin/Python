# Задача 26:  
# Посчитать факториал (произведение 1 до N) 
# и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def Factorial(n):
    if n in [0, 1]:
        return 1
    return Factorial(n-1)*n 

def Triangle(n):
    if n == 0:
        return 0
    return Triangle(n-1)+n   

print(Factorial(5))
print(Triangle(5))