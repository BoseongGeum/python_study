import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
inequs = input().split()

numbers = permutations([i for i in range(10)], n+1)

def check(number):
    for i in range(n):
        if inequs[i] == '<' and number[i] > number[i+1]:
            return False
        elif inequs[i] == '>' and number[i] < number[i+1]:
            return False
        
    return True

for number in numbers:
    if check(number):
        minNumber = map(str, number)
        break

for number in list(numbers)[::-1]:
    if check(number):
        maxNumber = map(str, number)
        break

print(''.join(maxNumber))
print(''.join(minNumber))
