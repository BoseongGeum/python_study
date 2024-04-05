import sys
input = sys.stdin.readline

while True:
    bit = input().rstrip()
    
    if bit == '#':
        break
    
    elif bit[-1] == 'e':
        c = 0
        for n in bit:
            if n == '1':
                c += 1
        if c % 2 == 0:
            print(bit[:len(bit)-1] + '0')
        else:
            print(bit[:len(bit)-1] + '1')
    else:
        c = 0
        for n in bit:
            if n == '1':
                c += 1
        if c % 2 == 0:
            print(bit[:len(bit)-1] + '1')
        else:
            print(bit[:len(bit)-1] + '0')
