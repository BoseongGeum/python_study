import sys
input = sys.stdin.readline

def maxmax():
    subsum = -1000
    maxsum = -1000
    for x in numlist:
        if subsum + x > x:
            subsum += x
        else:
            subsum = x
        if maxsum < subsum:
            maxsum = subsum
    return print(maxsum)

n = int(input())
numlist = map(int, input().split())

maxmax()
