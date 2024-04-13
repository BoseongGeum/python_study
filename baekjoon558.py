import sys
input = sys.stdin.readline

l = sorted(list(map(int, input().split())))

if l[1] - l[0] == l[2] - l[1]:
    print(2 * l[2] - l[1])
elif l[1] - l[0] < l[2] - l[1]:
    print(2 * l[1] - l[0])
else:
    print(l[0] + l[2] - l[1])
