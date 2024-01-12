import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = input().rstrip()
    result = str(int(n) + int(n[::-1]))

    flag = True
    for i in range(len(result)//2):
        if result[i] != result[len(result)-1-i]:
            flag = False

    if flag:
        print('YES')
    else:
        print('NO')
