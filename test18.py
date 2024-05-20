from itertools import permutations
import math

def solution(numbers):
    max_number = ''.join(sorted(numbers)[::-1])
    primes = {i:True for i in range(2, int((int(max_number)+1)**(1/2)))}
    primes[0] = primes[1] = False
    
    for i in range(2, int(max_number)+1):
        for j in range(2, int(max_number)//i+1):
            primes[i*j] = False
    
    number_list = []
    for n in numbers:
        number_list.append(n)
    
    all_numbers = []
    for i in range(1, len(numbers)+1):
        permu_numbers = list(permutations(number_list, i))
        for p in permu_numbers:
            all_numbers.append(int(''.join(p)))
    all_numbers = list(set(all_numbers))
    print(all_numbers)
    print(primes)
    
    count = 0
    for n in all_numbers:
        if primes[n] == True:
            count += 1
    
    return count
