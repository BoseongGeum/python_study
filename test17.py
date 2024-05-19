def solution(answers):
    result = []
    acount = bcount = ccount = 0
    a = [1,2,3,4,5] * ((10000//5) + 5)
    b = [2,1,2,3,2,4,2,5] * ((10000//8) + 8)
    c = [3,3,1,1,2,2,4,4,5,5] *((10000//10) + 10)
    
    for i in range(len(answers)):
        if answers[i] == a[i]:
            acount += 1
        if answers[i] == b[i]:
            bcount += 1
        if answers[i] == c[i]:
            ccount += 1
    
    counts = [acount, bcount, ccount]
    for i in range(len(counts)):
        if counts[i] == max(counts):
            result.append(i+1)
    
    return result
