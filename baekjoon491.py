import sys
input = sys.stdin.readline

l = [float(input())]
i = 0
while True:
    f = float(input())
    if f == 999:
        break
    l.append(f)
    print(f'{l[i+1] - l[i]:.2f}')
    i += 1
