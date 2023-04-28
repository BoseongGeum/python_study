import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
        continue
    c = 0
    
    for i in range(n + 1, 2 * n):
        if i == 2:
            c += 1
            continue
        
        for j in range(2, i):
            if i % j == 0:
                break
            if j * j > i:
                c += 1
                break

    print(c)
