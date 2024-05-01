import sys
input = sys.stdin.readline

GA = [1, 2, 3, 3, 4, 10]
TA = [1, 2, 2, 2, 3, 5, 10]

n = int(input())
for i in range(n):
    gaNum = list(map(int, input().split()))
    taNum = list(map(int, input().split()))

    gaNumTot = taNumTot = 0
    for j in range(len(GA)):
        gaNumTot += gaNum[j] * GA[j]
    for j in range(len(TA)):
        taNumTot += taNum[j] * TA[j]

    if gaNumTot > taNumTot:
        print(f'Battle {i+1}: Good triumphs over Evil')
    elif gaNumTot < taNumTot:
        print(f'Battle {i+1}: Evil eradicates all trace of Good')
    else:
        print(f'Battle {i+1}: No victor on this battle field')
