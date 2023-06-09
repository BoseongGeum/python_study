import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    i = 1
    j = n - 1
    l = []
    while i < j:
        l.append([i, j])
        i += 1
        j -= 1

    p = ''
    for x in l:
        p += f' {x[0]} {x[1]}'
        if x != l[-1]:
            p += ','
    print(f'Pairs for {n}:{p}')
