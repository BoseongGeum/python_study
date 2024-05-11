from heapq import *

def solution(operations):
    answer = []
    heap = []
    
    for operation in operations:
        oper, num = operation[0], int(operation[2:])

        if oper == 'D':
            if len(heap) == 0:
                continue
            elif num == -1:
                heappop(heap)
            else:
                temp_heap = []
                while heap:
                    if len(heap) == 1:
                        heappop(heap)
                        break
                    heappush(temp_heap, heappop(heap))
                heap = temp_heap[::]
                    
        else:
            heappush(heap, num)
        print(heap)

    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer = [max(heap), min(heap)]
    
    return answer

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))
