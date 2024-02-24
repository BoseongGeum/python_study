import sys
input = sys.stdin.readline

event = [[9.23076, 26.7, 1.835], [1.84523, 75, 1.348], [56.0211, 1.5, 1.05], [4.99087, 42.5, 1.81], [0.188807, 210, 1.41], [15.9803, 3.8, 1.04], [0.11193, 254, 1.88]]
n = int(input())
for _ in range(n):
    p = list(map(int, input().split()))
    s = 0
    for i in range(7):
        s += int(event[i][0] * abs(event[i][1] - p[i]) ** event[i][2])
    print(s)
