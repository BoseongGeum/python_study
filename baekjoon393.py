import sys
input = sys.stdin.readline

l = list(map(int, input().split()))

while l != [1, 2, 3, 4, 5]:
    for i in range(4):
        if l[i] > l[i+1]:
            tmp = l[i]
            l[i] = l[i+1]
            l[i+1] = tmp
            print(*l)
