import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    
    if n == '0':
        break
    s = 1
    for i in range(len(n) // 2):
        if n[i] != n[len(n) - 1 - i]:
            s = 0
            break
    if s == 1:
        print('yes')
    else:
        print('no')
