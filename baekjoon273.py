import sys
input = sys.stdin.readline

n = list(map(int, input().split()))

s = 0
for x in n:
    s += x ** 2
    
print(s % 10)
