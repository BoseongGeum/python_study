import sys
input = sys.stdin.readline

n, m = map(int,input().split())
Eyfa = True
ori = ['' for _ in range(n)]
mod = ori[::]
for i in range(n):
    ori[i] = input().rstrip()
for i in range(n):
    mod[i] = input().rstrip()
for i in range(n):
    if mod[i][::2] == mod[i][1::2] == ori[i]:
        continue
    else:
        Eyfa = False
        break

if Eyfa == True:
    print('Eyfa')
else:
    print('Not Eyfa')
