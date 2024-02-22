import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    n = int(input())
    data = input().rstrip()
    for exe in data:
        if exe == 'c':
            n += 1
        else:
            n -= 1
    print(f'Data Set {i}:\n{n}')
    if i != t:
        print()
