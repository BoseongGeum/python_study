import sys
input = sys.stdin.readline

mod = 1000000007

def fact(n):
    result = 1
    
    for i in range(2, n+1):
        result = (result * i) % mod

    return result

n, k = map(int, input().split())

if k == 0 or k == n:
    print(1)
    
else:
    a = fact(n)
    b = (fact(k) * fact(n-k)) % mod
    
    print((a * pow(b, mod-2, mod)) % mod)
