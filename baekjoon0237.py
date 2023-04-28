import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    if n < 3:
        print(2)
        
    else:
        a = n
        r = 0
        while r == 0:
            for i in range(2, n):
                if a % i == 0:
                    a += 1
                    break
                if i * i > n:
                    r = a
                    break

        print(r)
