def solution(citations):
    answer = 0
    total = 0
    hIndex = [0 for i in range(max(citations)+1)]
    for cit in citations:
        hIndex[cit] += 1
    for i in range(1, len(hIndex))[::-1]:
        total += hIndex[i]
        if total >= i:
            answer = i
            break
    
    return answer
