a, b, c = map(int, input().split())
l = [a, b, c]
l.sort()

if l[0] == l[1] and l[1] == l[2]:
    print(10000+l[1]*1000)
elif (l[0] != l[1] and l[1] == l[2]) or (l[0] == l[1] and l[1] != l[2]):
    print(1000+l[1]*100)
else:
    print(l[-1]*100)
