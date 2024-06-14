from collections import defaultdict

def solution(tickets):

    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
        
    for key in graph.keys():
        graph[key].sort(reverse=True)

    route = []

    def dfs(city):
        while graph[city]:
            dfs(graph[city].pop())
        route.append(city)

    dfs("ICN")
    return route[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
