def solution(distance, rocks, n):
    rocks = [0] + sorted(rocks) + [distance]
    start, end = 0, distance
    min_distance = distance

    while start <= end:
        mid = (start + end) // 2
        j = 0
        count = 0
        
        for i in range(1, len(rocks)):
            if rocks[i] - rocks[j] >= mid:
                j = i
            else:
                count += 1
        print(start, mid, end)
                
        if count > n:
            end = mid - 1
        else:
            start = mid + 1
    
    return start - 1

print(solution(12, [2, 4, 6, 8, 10], 2))
print(solution(25, [2, 11, 14, 17, 21], 2))
