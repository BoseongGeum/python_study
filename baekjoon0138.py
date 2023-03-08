import sys
input = sys.stdin.readline
sys.setrecrusionlimit(1000000)

def bi(left, right):
    mid = (left + right) // 2
    
    if left >= right:
        return -1
    
    if dp[mid] < l[x] <= dp[mid + 1]:
        return mid + 1
    
    if l[x] > dp[mid]:
        return bi(mid+1, dplength)
    
    if l[x] < dp[mid]:
        return bi(0, mid-1)


n = int(input())
l = list(map(int, input().split()))
dp = [0, l[0]]
dplength = 1


for x in range(1, n):
    
    if l[x] in dp:
        continue
    
    index = bi(0, dplength)
    
    if index == -1:
         dp.append(l[x])
         dplength += 1
         
    else:
        dp[index] = l[x]
        
print(dplength)
