def solution(word):
    dic = []
    for fir in ['A', 'E', 'I', 'O', 'U']:
        for sec in ['.', 'A', 'E', 'I', 'O', 'U']:
            for thi in ['.', 'A', 'E', 'I', 'O', 'U']:
                if sec == '.' and thi != '.':
                    continue
                for fou in ['.', 'A', 'E', 'I', 'O', 'U']:
                    if thi == '.' and fou != '.':
                        continue
                    for fif in ['.', 'A', 'E', 'I', 'O', 'U']:
                        if fou == '.' and fif != '.':
                            continue
                        dic.append(fir + sec + thi + fou + fif)
    dic.sort()
    
    word += '.' * (5 - len(word))
    for i in range(len(dic)):
        if word == dic[i]:
            return i+1

word = 'UUUUU'
print(solution(word))
