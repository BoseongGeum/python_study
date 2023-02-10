import string

s = input()
d = {}
a = 48
for x in list(map(str, range(10))):
    d[x] = a
    a += 1
y = 97
for x in string.ascii_lowercase:
    d[x] = y
    y += 1
z = 65
for x in string.ascii_uppercase:
    d[x] = z
    z += 1
print(d[s])
