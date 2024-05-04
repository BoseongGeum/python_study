from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    stack = deque()

    while queue:
        p = queue.popleft()
        time = 0
        for _ in range(len(queue)):
            time += 1
            stack.append(queue.popleft())
            if p > stack[-1]:
                break
        while stack:
            queue.appendleft(stack.pop())
        answer.append(time)
        print(queue)
        
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))
