import sys
input = sys.stdin.readline

for _ in range(3):
    n = input().rstrip()
    m = maxm = 1
    for i in range(7):
        if n[i] == n[i+1]:
            m += 1
            if m > maxm:
                maxm = m
        else:
            if m > maxm:
                maxm = m
            m = 1
    print(maxm)
