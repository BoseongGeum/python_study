import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l =[]
    count = 0
    p, m = map(int, input().split())
    for _ in range(p):
        i = int(input())
        if i in l:
            count +=1
        else:
            l.append(i)
    print(count)
