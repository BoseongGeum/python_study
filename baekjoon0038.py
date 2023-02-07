import sys

a = [sys.stdin.readline().strip() for _ in range(28)]
b = list(map(int, a))
c = list(range(1,31))
stu = [x for x in c if x not in b]
print(stu[0])
print(stu[1])
