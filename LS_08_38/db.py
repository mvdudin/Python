def connect(fname):
    try:
        book = open(fname, 'r')
    except IOError:
        book = open(fname, 'w')
    finally:
        book.close()

def insert(fname):
    book = open(fname, 'a')
    book.write(str(input("Введите ФИО и номер телефона через пробел ")) + "\n")
    book.close()

def show(fname):
    book = open(fname, "r")
    for row in book:
        print(row[:-1])
    book.close()

def search(fname):
    found = 0
    book = open(fname, 'r')
    fio = str(input("Введите фамилию:"))
    for row in book:
        if fio in row:
            print(row)
            found+=1
    book.close()
    if found == 0:
        print("Абонент не найден")
    

def edit(fname):
    found = 0
    file = open(fname, 'r')
    book = [row for row in file]
    file.close()
    fio = str(input("Введите фамилию абонента которого надо изменить:"))
    for i in range (0, len(book)):
        if fio in book[i]:
            found+=1
            book[i] = str(input("Введите ФИО и номер телефона через пробел "))
    if found > 0:
        file = open(fname, 'w')
        for r in book:  
            file.write(r)
        file.close()    
    else:
        print("Абонент не найден")
    
def delete(fname):
    file = open(fname, 'r')
    book = [row for row in file]
    file.close()
    deleted = 0
    fio = str(input("Введите фамилию абонента которого надо удалить:"))
    for r in book:
        if fio in r:
            book.remove(r)
            print('Удалён ', r)
            deleted+=1
    if deleted > 0:
        file = open(fname, 'w')
        for r in book:  
            file.write(r)
        file.close()    
    else:
        print("Абоненты не найдены")