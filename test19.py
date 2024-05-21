def solution(brown, yellow):
    total = brown // 2 - 2
    for h in range(1, total+1):
        if h * (total - h) == yellow:
            return [total - h + 2, h + 2]
