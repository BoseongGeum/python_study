import string

s = input()

dic = {}
l = []
for x in string.ascii_lowercase:
    if x in s:
        x = s.index(x)
        l.append(x)
    else:
        x = -1
        l.append(x)

for x in l:
    print(x, end=' ')
