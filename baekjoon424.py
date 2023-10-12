import sys
input = sys.stdin.readline

n = int(input())

money = []
for _ in range(n):
    l = sorted(list(map(int, input().split())))
    
    if l.count(l[0]) == 4:
        money.append(50000 + l[0] * 5000)
    elif l.count(l[0]) == 3 or l.count(l[1]) == 3:
        money.append(10000 + l[1] * 1000)
    elif l.count(l[0]) == 2 and l.count(l[2]) == 2:
        money.append(2000 + (l[0] + l[2]) * 500)
    elif l.count(l[0]) == 2:
        money.append(1000 + l[0] * 100)
    elif l.count(l[2]) == 2:
        money.append(1000 + l[2] * 100)
    else:
        money.append(max(l) * 100)

print(max(money))
