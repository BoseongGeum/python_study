import sys
input = sys.stdin.readline

n = input().rstrip()
l = {'000':0, '001':1, '010':2, '011':3, '100':4, '101':5, '110':6, '111':7}

i = len(n) % 3
if i != 0:
    n = '0' * (3 - i) + n

for j in range(len(n) // 3):
    print(l[n[j*3:j*3+3]], end='')
print()
