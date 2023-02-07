import sys

num = [sys.stdin.readline().strip() for _ in range(10)]
my_num = list(map(int, num))
val = []

for x in my_num:
    rest = x % 42
    if rest in val:
        pass
    else:
        val.append(rest)
        
print(len(val))
