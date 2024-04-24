import sys
input = sys.stdin.readline

n = input().rstrip()
print(bin(int('0o' + n, 8))[2:])
