import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    result = (a + b) * (b - a + 1) // 2
    print(f'Scenario #{i+1}:')
    print(result)
    if i != n - 1:
        print()
