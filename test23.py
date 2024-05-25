def solution(n, times):
    # 심사대의 최소 시간과 최대 시간을 초기화
    left, right = 1, max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        
        # mid 시간 내에 처리할 수 있는 총 사람 수
        total = sum(mid // time for time in times)
        
        # 총 처리한 사람이 n명 이상이면 시간을 줄여본다
        if total >= n:
            right = mid
        else:
            left = mid + 1
            
    return left

times = [1, 1, 1]
n = 59
print(solution(n, times))
