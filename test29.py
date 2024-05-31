def solution(n, costs):
    answer = 0
    islands = {i:i for i in range(n)}

    for cost in costs:
        cost[0], cost[1], cost[2] = cost[2], cost[0], cost[1]
    costs.sort()
    
    for cost in costs:
        if islands[cost[1]] == islands[cost[2]]:
            continue
        else:
            islands[cost[1]] = min(islands[cost[1]], islands[cost[2]])
            islands[cost[2]] = min(islands[cost[1]], islands[cost[2]])
            answer += cost[0]
    
    return answer

costs =  [[0,1,1],[0,2,2],[2,1,5],[1,3,1],[2,3,8]]
print(solution(4, costs))
