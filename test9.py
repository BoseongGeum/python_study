from heapq import *

def solution(jobs):
    answer = 0
    count = len(jobs)
    heapify(jobs)
    ready = []

    while jobs or ready:
        if len(ready) == 0:
            job = heappop(jobs)
            time = job[0] + job[1]
            answer += time - job[0]
        else:
            job = heappop(ready)
            time += job[0]
            answer += time - job[1]
        
        while jobs:
            temp = heappop(jobs)
            if temp[0] <= time:
                heappush(ready, [temp[1],temp[0]])
            else:
                heappush(jobs, temp)
                break

        print(time)
        print(answer)
    
    return answer // count

jobs = [[1, 1], [1, 1], [5, 3]]
print(solution(jobs))
