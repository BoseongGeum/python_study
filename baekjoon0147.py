import sys
input = sys.stdin.readline

n = int(input())
dp = [1]*(n+1)
l = list(map(int, input().split()))

