def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people)-1
    
    while i <= j:
        if limit - 40 < people[j]:
            answer += 1
            j -= 1
            continue
            
        if people[i] + people[j] <= limit:
            answer += 1
            i += 1
            j -= 1
        
        else:
            answer += 1
            j -= 1
            
    return answer
