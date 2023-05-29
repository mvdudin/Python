items = []
items.insert(0, "1 - Добавление нового контакта")
items.insert(1, "2 - Вывод всех контактов на экран")
items.insert(2, "3 - Поиск контакта по фамилии")
items.insert(3, "4 - Редактровать контакт по фамилии")
items.insert(4, "5 - Удалить контакт по фамилии")
items.insert(5, "6 - Выход")

def ActionCode():
    for i in items:
        print(i)
    return int(input("Введите код действия: "))