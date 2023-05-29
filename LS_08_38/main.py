# 55.  Создать телефонный справочник 
# с возможностью импорта и экспорта данных в формате .txt.
# Поля справочника Фамилия, имя, отчество, номер телефона

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии

from menu import ActionCode
import db as db
db_name = 'db1.txt'
db.connect(db_name)
while True:
    match ActionCode():
        case 1:
            db.insert(db_name)
        case 2:
            db.show(db_name)
        case 3:
            db.search(db_name)
        case 4:
            db.edit(db_name)
        case 5:
            db.delete(db_name)            
        case 6:
            break
