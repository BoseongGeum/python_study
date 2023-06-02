import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = input().split()
    for x in l[:len(l)-1]:
        print(x[::-1], end=' ')
    print(l[-1][::-1])
