def get_shop_list_by_dishes(dishes, person_count):
    global cook_book
    res = {}
    for i in dishes:
        for n in cook_book[i]:
            res.setdefault(n['ingredient_name'])
            res[n['ingredient_name']] = {'measure': '', 'quantity': 0}
            res[n['ingredient_name']]['measure'] = n['measure']
            res[n['ingredient_name']]['quantity'] += int(n['quantity'])*int(person_count)
    return(res)

with open('file.txt', 'r', encoding='utf-8') as txt:
    spisok = txt.read()
spisok = spisok.split('\n\n')
cook_book = {}
for i in spisok:
    spisok[spisok.index(i)] = spisok[spisok.index(i)].split('\n')

for i in spisok:
    for n in i[1:]:
        spisok[spisok.index(i)][spisok[spisok.index(i)].index(n)] = spisok[spisok.index(i)][spisok[spisok.index(i)].index(n)].split(' | ')

for i in spisok:
    cook_book.setdefault(i[0])
    cook_book[i[0]] = []
    for n in i[2:]:
        cook_book[i[0]].append({'ingredient_name': n[0],'quantity': n[1],'measure': n[2]})

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))