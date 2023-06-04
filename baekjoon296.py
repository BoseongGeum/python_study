import sys
input = sys.stdin.readline

n = input().rstrip()

length = len(n)
s = (int(n) - int('1' + '0' * (length-1)) + 1) * length
length -= 1
for _ in range(length):
    s += int('9' + '0' * (length-1)) * length
    length -= 1

print(s)
