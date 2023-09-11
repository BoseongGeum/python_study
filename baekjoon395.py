import sys
input = sys.stdin.readline

e, f, c = map(int, input().split())

ex = (e + f) // c
re = (e + f) % c + ex
count = ex

while re >= c:
    ex = re // c
    re = re % c + ex
    count += ex

print(count)
