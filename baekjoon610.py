import sys
input = sys.stdin.readline
        
n = int(input())

numbers = ['1','2','3']

def is_good_sequence(sequence):
    
    for i in range(1, len(sequence)//2+1):
        if sequence[-i:] == sequence[-i*2:-i]:
            return False
        
    return True

def dfs(sequence):    

    if len(sequence) == n:
        print(sequence)
        return True
    
    for number in numbers:
        new_sequence = sequence + number
        
        if is_good_sequence(new_sequence):
            if dfs(new_sequence):
                return True

    return False

dfs('')
