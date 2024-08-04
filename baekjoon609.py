import sys
input = sys.stdin.readline

n, l = map(int, input().split())
holes = sorted(map(int, input().split()))

start = count = 0
while start < n:
    end = start + 1
    
    while end < n and holes[end] - holes[start] < l:
        end += 1

    count += 1
    start = end

print(count)
