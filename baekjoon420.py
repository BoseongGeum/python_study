import sys
from string import ascii_lowercase
input = sys.stdin.readline

while True:
    alphabet_dict = {v:0 for v in ascii_lowercase}
    pangram = True
    
    sentence = input().rstrip()
    
    if sentence == '*':
        break

    for a in sentence:
        alphabet_dict[a] = 1

    for b in alphabet_dict.values():
        if b == 0:
            pangram = False
            break

    if pangram == True:
        print('Y')
    else:
        print('N')
