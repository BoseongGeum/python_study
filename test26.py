def solution(name):
    x = y = answer = minMove = 0
    
    for i in range(len(name)):
        if name[i] != 'A':
            minMove = len(name) - i
            break
    for i in range(len(name))[::-1]:
        if name[i] != 'A':
            minMove = min(minMove, i)
            break
    
    for i in range(len(name)):
        for j in range(i+1, len(name)):
            if name[i] != 'A' and name[j] != 'A':
                x = i
                y = len(name) - j
                minMove = min(minMove, 2*x+y, 2*y+x)
                break
                
    answer += minMove
    print(answer)
    
    
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A'), 26 - ord(name[i]) + ord('A'))
        
    return answer
