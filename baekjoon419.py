import sys
input = sys.stdin.readline


r = int(input())
s = input().rstrip()

while True:

    if s == '=':
        print(r)
        break
    
    i = int(input())

    if s == '+':
        r += i

    elif s == '-':
        r -= i

    elif s == '*':
        r *= i

    else:
        r //= i
    
    s = input().rstrip()
        
