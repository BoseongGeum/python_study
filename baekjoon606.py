import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())
    except:
        break
    
    n = int(input())
    blocks = [0 for _ in range(n)]
    for i in range(n):
        blocks[i] = int(input())

    blocks.sort()

    x *= 10000000
    start, end = 0, n-1
    danger = True

    while start < end:
        if blocks[start] + blocks[end] < x:
            start += 1
        elif blocks[start] + blocks[end] > x:
            end -= 1
        else:
            print('yes', blocks[start], blocks[end])
            danger = False
            break
        
    if danger:
        print('danger')
