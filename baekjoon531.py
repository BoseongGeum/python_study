import sys
input = sys.stdin.readline

n = int(input())
one = [0,"Yakk","Doh","Seh","Ghar","Bang","Sheesh"]
double = [0,"Habb Yakk","Dobara","Dousa","Dorgy","Dabash","Dosh"]
for i in range(1, n+1):
    a, b = map(int, input().split())
    if a == b:
        print(f'Case {i}: {double[a]}')
    else:
        if a == 5 and b == 6 or a == 6 and b == 5:
            print(f'Case {i}: Sheesh Beesh')
        else:
            print(f'Case {i}: {one[max(a,b)]} {one[min(a,b)]}')
