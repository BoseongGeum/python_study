import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
t = int(input())

ps = t % 60
pm = (t // 60) % 60
ph = t // 3600

s = s + ps
m = m + pm + s // 60
h = h + ph + m // 60

print(h % 24, m % 60, s % 60)
