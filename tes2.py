from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridgeQueue = deque([0] * bridge_length)
    readyQueue = deque(truck_weights)
    count = 0
    total = 0
    
    while readyQueue:
        temp = readyQueue.popleft()
        if total + temp - bridgeQueue[-1] <= weight and count <= bridge_length:
            bridgeQueue.appendleft(temp)
            count += 1
            total += temp
        else:
            readyQueue.appendleft(temp)
            bridgeQueue.appendleft(0)
        temp = bridgeQueue.pop()
        if temp != 0:
            count -= 1
            total -= temp
        answer += 1
        
    return answer + bridge_length
