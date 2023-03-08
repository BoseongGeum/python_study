import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
dp = [l[0]]

def bi(left, right):
    mid = (left + right) // 2
    if dp[mid] < l[x] <= dp[mid + 1]:
        return mid + 1
    if dp[mid] < l[x]:
        return bi(mid, len(dp)-1)
    if dp[mid] >= l[x]:
        return bi(0, mid)

for x in range(1, n):
    if l[x] > max(dp):
        dp.append(l[x])
    if dp[0] < l[x] <= max(dp):
        dp[bi(0, len(dp)-1)] = l[x]
    if l[x] <= dp[0]:
        dp[0] = l[x]

print(len(dp))
