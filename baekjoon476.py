import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    front, back = input().split('-')
    front_value = (ord(front[0])-ord('A'))*26**2 + (ord(front[1])-ord('A'))*26 + ord(front[2])-ord('A')
    back_value = int(back)

    if abs(front_value - back_value) <= 100:
        print('nice')
    else:
        print('not nice')
