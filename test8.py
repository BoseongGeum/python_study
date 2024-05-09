from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while len(scoville) != 1:
        temp = heappop(scoville)
        if temp >= K:
            break
        heappush(scoville, temp + heappop(scoville) * 2)
        answer += 1

    if heappop(scoville) < K:
        answer = -1
        
    return answer
