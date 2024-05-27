def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    count = -len(lost)
    for i in range(1, n+1):
        if i in lost and i in reserve:
            count += 1
            reserve.remove(i)
            lost.remove(i)
    for i in range(1, n+1):
        if i in lost and i-1 in reserve:
            count += 1
            reserve.remove(i-1)
            lost.remove(i)
        elif i in lost and i+1 in reserve:
            count += 1
            reserve.remove(i+1)
            lost.remove(i)
        
    return n + count
