import sys
input = sys.stdin.readline

n = int(input())
result = input().rstrip()
for _ in range(n-1):
    s = input().rstrip()
    for i in range(len(result)):
        if result[i] != s[i]:
            result = result[:i] + '?' + result[i+1:]

print(result)
