def solution(nums):
    answer = 0
    phone = {}
    
    for n in nums:
        if n in phone:
            phone[n] += 1
        else:
            phone[n] = 0
            answer += 1
    
    if answer > len(nums) // 2:
        answer = len(nums) // 2
        
    return answer
