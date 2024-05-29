def solution(number, k):
    answer = ''
    answer_len = len(number) - k
    len_full = False
    
    while k > 0:
        if len(answer) >= answer_len:
            len_full = True
            break
        
        n = number[0]
        i = 0
        for index in range(len(number[:k+1])):
            if n == 9:
                i = index
                break
            if n < number[index]:
                n = number[index]
                i = index
            
        number = number[i+1:]
        k -= i
        answer += n

    if len_full == True:
        number = ''
        
    return answer + number
