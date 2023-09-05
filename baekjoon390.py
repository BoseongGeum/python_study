import sys
input = sys.stdin.readline

n, l = map(int, input().split())
f = sorted(list(map(int, input().split())))

for i in f:
    if i <= l:
        l += 1
    else:
        break
    
print(l)
