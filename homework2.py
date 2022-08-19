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
slovar_sorted = {}
sorted_lens = sorted(slovar.values())
for i in sorted_lens:
    for n in slovar:
        if slovar[n] == i:
            slovar_sorted.setdefault(n, slovar[n])
            break
print(slovar_sorted)
with open('result_txt.txt', 'w', encoding='utf-8') as f:
    for i in slovar_sorted:
        with open(i, encoding='utf-8') as f1:
            txt = f1.read()
        f.writelines(i+'\n')
        f.writelines(str(slovar_sorted[i])+'\n')
        f.writelines(txt+'\n')
