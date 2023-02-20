a = int(input())
l = []
for x in range(a - 9*len(str(a)), a):
    if x > 0 and x + sum(map(int, list(str(x)))) == a:
        l.append(x)
if l == []:
    print(0)
else:
    print(min(l))
