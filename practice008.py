n = int(input())
k = int(input())

def biin(n, k):

    if k == 0 or k == n:
        return 1

    else:
        return biin(n-1, k-1) + biin(n-1, k)

print(biin(n, k))
