import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
n_l = list(reversed([i for i in range(1, n+1)]))
stack  = [0]
c_l = []
a = True

def push(x):
    while True:
        if stack[-1] == x:
            break
            
        stack.append(n_l.pop())
        c_l.append('+')
        
def pop(x):
    stack.pop()
    c_l.append('-')

for x in l:

    if stack[-1] > x:
        a = False
        break
    
    push(x)
    pop(x)
    
if a == False:
    print('NO')

else:
    for x in c_l:
        print(x)
