from itertools import permutations

def solution(k, dungeons):
    all_case = permutations(dungeons, len(dungeons))
    max_result = 0
    
    for case in all_case:
        result = 0
        temp_k = k
        for d in case:
            if temp_k >= d[0]:
                temp_k -= d[1]
                result += 1
            else:
                break
                
        if result == len(dungeons):
            return result
        elif result > max_result:
            max_result = result
            
    return max_result
