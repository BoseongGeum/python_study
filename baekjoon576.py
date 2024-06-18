import sys
input = sys.stdin.readline

stack = []

n = int(input())

for _ in range(n):
    c = input().rstrip()
    
    if c[0] == '1':
        stack.append(c[2:])
        
    elif c == '2':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
            
    elif c == '3':
        print(len(stack))
        
    elif c == '4':
        if stack == []:
            print(1)
        else:
            print(0)

    elif c == '5':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
        
