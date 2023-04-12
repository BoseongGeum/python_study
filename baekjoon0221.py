import sys
input = sys.stdin.readline

n = int(input())
l = []
overlap = 0

for _ in range(n):
    m = int(input())

    q = m // 25
    d = (m % 25) // 10
    ni = ((m % 25) % 10) // 5
    p = ((m % 25) % 10) % 5
    
    print (q, d, ni, p)
