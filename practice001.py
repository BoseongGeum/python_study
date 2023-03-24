n = int(input())
l = list(map(int, input().split()))
x = int(input())

def binsearch(left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if x == l[mid]:
        return mid

    elif x > l[mid]:
        return binsearch(mid + 1, right)

    else:
        return binsearch(left, mid - 1)

print(binsearch(0, n - 1))
