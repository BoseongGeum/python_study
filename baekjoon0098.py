import sys

n, m = map(int, input().split())
s1 = {sys.stdin.readline().rstrip() for x in range(n)}
s2 = {sys.stdin.readline().rstrip() for x in range(m)}

print(len(s1&s2), *sorted(s1&s2), sep='\n')
