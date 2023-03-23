import sys
input = sys.stdin.readline

n = int(input())

def devide(i, left, right):
    if left > right:
        return left
    
    mid = (left + right) // 2
    
    if i > l[mid]:
        return devide(i, mid + 1, right)
    else:
        return devide(i, left, mid - 1)

l = [int(input())]
print(l[0])
for x in range(1, n):
    i = int(input())
    l.insert(devide(i, 0, x-1), i)
    
    print(l[x//2])
