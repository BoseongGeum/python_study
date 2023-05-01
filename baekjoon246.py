import sys
input = sys.stdin.readline          
    
t = int(input())

for _ in range(t):
    total = int(input())
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        total += a * b
        
    print(total)
