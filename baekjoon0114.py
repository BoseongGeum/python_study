import sys
input = sys.stdin.readline

n,m = map(int, input().split())
visited = [False for _ in range(n+1)]
l = []

def back():
    if len(l) == m and l == sorted(l):
        print(*l)
        return
    for x in range(1, n+1):
        if visited[x] == False:
            visited[x] = True
            l.append(x)
            back()
            l.pop()
            visited[x] = False
                        
back()
