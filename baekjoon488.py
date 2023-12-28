import sys
input = sys.stdin.readline

a, b = input().split()

maxlen = max(len(a), len(b))
minlen = min(len(a), len(b))
gap = maxlen - minlen

if maxlen == len(a):
    b = '0' * gap + b
else:
    a = '0' * gap + a

result = ''
for i in range(maxlen):
    result += str(int(a[i]) + int(b[i]))

print(result)
