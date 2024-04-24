import sys
input = sys.stdin.readline

n = input().rstrip()
print(oct(int('0b' + n, 2))[2:])
