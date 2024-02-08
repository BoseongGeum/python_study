import sys
input = sys.stdin.readline

numbers = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    temp = numbers[::]
    for i in range(a, b+1):
        numbers[i] = temp[b+a-i]

print(*numbers[1:])
