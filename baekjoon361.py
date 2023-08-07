import sys
input = sys.stdin.readline

u, t, uo, to = map(int, input().split())
print(u * 56 + t * 24 + uo * 14 + to * 6)
