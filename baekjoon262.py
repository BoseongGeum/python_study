import sys
input = sys.stdin.readline          

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(n):
    
    if a[i] >= b[i]:
        continue
    g = b[i] - a[i]
    c = g//30 + 1
    a[i] += 30 * c
    count += c
    for j in range(n):
        if b[i] < b[j] and a[i] > a[j]:
            c = (a[i] - a[j])//30 + 1
            a[j] += 30 * c
            count += c

print(count)
