import sys
input = sys.stdin.readline

while True:
    
    s = input().rstrip()
    b = ''

    if s == '.':
        break

    for x in s:
        if x == '(' or x == ')' or x == '[' or x == ']':
            b += x

    while True:
        if not '()' in b and not '[]' in b:
            break
        
        b = b.replace('()', '').replace('[]', '')

    if b == '':
        print('yes')

    else:
        print('no')
