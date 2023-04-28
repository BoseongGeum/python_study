import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(n, m+1):
    if i == 1:
        continue
    if i == 2:
        print(i)
        continue
    
    for j in range(2, i):
        if i % j == 0:
            break
        if j * j > i:
            print(i)
            break
