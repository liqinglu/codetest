def reword(word):
    i = []
    for j in word:
        if j.isupper():
            i.append('_')
            i.append(j.lower())
        else:
            i.append(j)
    return ''.join(i[1:])


words = ['GetItem','DeRisk','SetLock']
for word in words:
    print reword(word)
