import sys
input = sys.stdin.readline

i = 1
while True:
    a, op, b = input().split()
    a, b = int(a), int(b)
    
    if op == '>' and a > b:
        print(f'Case {i}: true')
    elif op == '>=' and a >= b:
        print(f'Case {i}: true')
    elif op == '<' and a < b:
        print(f'Case {i}: true')
    elif op == '<=' and a <= b:
        print(f'Case {i}: true')
    elif op == '==' and a == b:
        print(f'Case {i}: true')
    elif op == '!=' and a != b:
        print(f'Case {i}: true')
    elif op == 'E':
        break
    else:
        print(f'Case {i}: false')
    i += 1
