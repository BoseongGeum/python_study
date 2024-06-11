from collections import deque

def solution(begin, target, words):
    queue = deque()
    visited = [False for i in range(len(words))]
    
    if target not in words:
        return 0
    
    for i in range(len(words)):
        for l in range(len(target)):
            if begin[:l] == words[i][:l] and begin[l+1:] == words[i][l+1:] and visited[i] == False:
                queue.append([words[i], 1])
                visited[i] = True

    while queue:
        change, count = queue.popleft()
        
        if change == target:
            return count
        
        for i in range(len(words)):
            for l in range(len(target)):
                if change[:l] == words[i][:l] and change[l+1:] == words[i][l+1:] and visited[i] == False:
                    queue.append([words[i], count+1])
                    visited[i] = True

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
