n = int(input('Размер n: '))
m = int(input('Размер m: '))
k = int(input('Хочу k долей: '))

if k <= m*n and (k%m==0 or k%n==0):
   print('Удача')
else:
   print('Нет вариантов')