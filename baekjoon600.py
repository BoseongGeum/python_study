import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

allA = permutations(a)

answer = 0

for aa in allA:
    tempAnswer = 0
    for i in range(n-1):
        tempAnswer += abs(aa[i] - aa[i+1])
        
    answer = max(answer, tempAnswer)

print(answer)
