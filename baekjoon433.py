import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = input().split()
    l = []
    
    for i in range(len(a)):
        if ord(a[i]) <= ord(b[i]):
            l.append(ord(b[i]) - ord(a[i]))
        else:
            l.append(ord(b[i]) - ord(a[i]) + 26)

    print("Distances: ", end="")
    print(*l)
