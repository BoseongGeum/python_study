import sys
input = sys.stdin.readline

n = int(input())
l = []

for i in range(n):

    if i == 0:
        num = int(input())
        l.append(num)
        print(num)
        continue

    
    num = int(input())
    s = 0
    e = i - 1
    while True:
        mid = (s + e) // 2

        if s > e:
            l.insert(mid + 1, num)
            break

        if num < l[mid]:
            e = mid - 1
        else:
            s = mid + 1

    now = i // 2
    print(l[now])
