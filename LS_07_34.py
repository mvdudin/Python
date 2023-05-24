##**Ввод:**  пара-ра-рам рам-пам-папам па-ра-па-да    
##**Вывод:** Парам пам-пам  

vovwel_rus = {'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е'}

def syllable(word):
    k=0
    for i in word:
        if i.lower() in vovwel_rus:
            k+=1
    return k        

poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
phrase = list(poem.split())
p = syllable(phrase[0])
phrase.pop(0)
phrase_f = list(filter(lambda x:syllable(x) == p, phrase))
if len(phrase) == len(phrase_f):
    print('Парам пам-пам')
else:
    print('Пам парам')

