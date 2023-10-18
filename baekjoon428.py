import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    l = sorted(list(map(int, input().split())))

    print(f"Scenario #{i+1}:")
    if l[2] ** 2 == l[0] ** 2 + l[1] ** 2:
        print("yes")
    else:
        print("no")
        
    if i + 1 != t:
        print()
