import sys
input = sys.stdin.readline

i = 1
while True:
    a = list(input().rstrip())
    b = input().rstrip()

    if b == 'END':
        break
    
    difference = False
    for v in b:
        if v in a:
            a.remove(v)
        else:
            difference = True
            break
        
    if difference:
        print(f'Case {i}: different')
    else:
        print(f'Case {i}: same')
    i += 1
