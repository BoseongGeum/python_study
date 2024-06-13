from collections import defaultdict

def solution(tickets):
    totalCount = len(tickets)
    visited = defaultdict(list)
    for k, v in tickets:
        visited[k].append(v)
    route = []
    
    def dfs(city, count):
        route.append(city)
        temp = []

        if len(route) > totalCount+1:
            return
        
        for i in range(len(tickets)):
            if tickets[i][0] == city and tickets[i][1] in visited[city]:
                temp.append(tickets[i][1])
        temp.sort()

        if count != totalCount and temp == []:
            route.pop()
            for ticket in tickets:
                visited[ticket[0]].append(ticket[1])
        print(visited)
        for nextCity in temp:
            visited[city].remove(nextCity)
            dfs(nextCity, count+1)


    dfs("ICN", 0)
           
    return route[:totalCount+1]

print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]))
