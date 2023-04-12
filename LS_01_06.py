
n = str(input('Номер билета 6 чифр: '))
s = 0
for i in 0,1,2:
    s +=  int(n[i])-int(n[-i-1])
  
if not s:
    print('Да будет вам счастье')    
else:
    print('Не ешь его )!')
