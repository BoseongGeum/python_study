import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    numDict = {str(k):0 for k in range(1, 10)}
    n = input().rstrip()
    for i in n:
        numDict[i] = 1
    print(list(numDict.values()).count(1))
