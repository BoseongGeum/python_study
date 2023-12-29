import sys
input = sys.stdin.readline
from string import ascii_lowercase
from string import ascii_uppercase

t = int(input())
for _ in range(t):
    dictionaryLower = {k:0 for k in ascii_lowercase}
    dictionaryUpper = {k:0 for k in ascii_uppercase}

    s = input().rstrip()
    for i in range(len(s)):
        if s[i] in ascii_lowercase:
            dictionaryLower[s[i]] = 1
        elif s[i] in ascii_uppercase:
            dictionaryUpper[s[i]] = 1

    missing = False
    for i in range(26):
        if list(dictionaryLower.values())[i] == 0 and list(dictionaryUpper.values())[i] == 0:
            if not missing:
                missing = True
                print('missing ', end = '')
            print(list(dictionaryLower.keys())[i], end = '')
    if not missing:
        print('pangram', end = '')
    print()
