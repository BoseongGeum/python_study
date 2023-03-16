import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    o = input().split()

    if o[0] == 'push':
        stack.append(o[1])

    elif o[0] == 'pop':
        if stack == []:
            print(-1)

        else:
            print(stack.pop())

    elif o[0] == 'size':
        print(len(stack))

    elif o[0] == 'empty':
        if stack == []:
            print(1)

        else:
            print(0)
    
    elif o[0] == 'top':
        if stack == []:
            print(-1)

        else:
            print(stack[-1])
