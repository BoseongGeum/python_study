import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = float(input())
    print(f'${round((p * 0.8), 2):.2f}')
