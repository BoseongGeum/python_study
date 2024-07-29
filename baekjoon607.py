import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n = int(input())
    pres = []
    possible = True
    for _ in range(n):

        num = input().rstrip()
        for pre in pres:
            if len(pre) <= len(num) and pre == num[:len(pre)]:
                possible = False
                break

        if possible == False:
            break

        pres.append(num)
        pres.sort()

    if possible == True:
        print('YES')
        
    else:
        print('NO')
