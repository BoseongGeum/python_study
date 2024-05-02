from collections import deque

priorities = [2,1,3,2]
location = 3

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    priorities = sorted(priorities)[::-1]
    print(queue, priorities)
    while queue:
        if queue[0] == priorities[0]:
            answer += 1

            if location == 0:
                return answer
            
            queue.popleft()
            del priorities[0]
            location -= 1
        else:
            queue.rotate(-1)
            location -= 1
        if location < 0:
            location += len(queue)

print(solution(priorities, location))
