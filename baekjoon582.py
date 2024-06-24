import sys
input = sys.stdin.readline

n = int(input())

frime = True

while True:
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            frime = False
            break
    
    if frime == True and str(n) == str(n)[::-1]:
        break

    frime = True
    n += 1

if n == 1:
    n += 1
    
print(n)
