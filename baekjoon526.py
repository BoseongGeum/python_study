import sys
input = sys.stdin.readline

while True:
    l = list(map(int, input().split()))
    if l == [0]:
        break
    for i in range(2, len(l)):
        if l[i-1] == l[i]:
            l[i-1] = 0
    while 0 in l:
        l.remove(0)
    print(*l[1:], '$')
