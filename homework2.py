import os
l = []
for file in os.listdir("texts"):
    if file.endswith(".txt"):
        l.append(file)
slovar = {}
for file in l:
    loc = 'texts/'+file
    with open(loc, encoding='utf-8') as f:
        txt = f.readlines()
        slovar.setdefault(loc, len(txt))
print(slovar)