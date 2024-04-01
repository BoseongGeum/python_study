import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a = input().rstrip()
    b = input().rstrip()
    r = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            r += 1
    print(f'Hamming distance is {r}.')
