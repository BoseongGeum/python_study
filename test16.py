def solution(sizes):
    w = 0
    h = 0
    
    for size in sizes:
        if min(size) > w:
            w = min(size)
        if max(size) > h:
            h = max(size)
    
    answer = w * h
    return answer
