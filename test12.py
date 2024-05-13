def solution(participant, completion):
    answer = ''
    parts = {}
    for k in participant:
        if k in parts:
            parts[k] += 1
        else:
            parts[k] = 1
    
    for c in completion:
        parts[c] -= 1
        print(parts)
    
    for p in participant:
        if parts[p] != 0:
            answer = p
            break
            
    return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))
