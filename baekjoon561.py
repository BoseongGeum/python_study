import sys
input = sys.stdin.readline

c = 0
for i in range(8):
    l = input().rstrip()
    for j in range(8):
        if l[j] == 'F':
            if i % 2 == 0 and j % 2 == 0:
                c += 1
            elif i % 2 == 1 and j % 2 == 1:
                c += 1

print(c)
