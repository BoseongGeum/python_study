import sys
input = sys.stdin.readline

num_count = {str(i):0 for i in range(10)}

s = 1
for _ in range(3):
    n = int(input())
    s *= n

for i in str(s):
    num_count[i] += 1

for i in num_count.values():
    print(i)
