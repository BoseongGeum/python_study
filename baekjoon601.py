import sys
input = sys.stdin.readline
from string import ascii_upppercase

r, c = map(int, input().split())

answer = 0

for aa in allA:
    tempAnswer = 0
    for i in range(n-1):
        tempAnswer += abs(aa[i] - aa[i+1])
        
    answer = max(answer, tempAnswer)

print(answer)
