import sys
input = sys.stdin.readline

n,m = map(int, input().split())
visited = [False for _ in range(n+1)]
l = []

def back():
    if len(l) == m:
        print(*l)
        return
    for x in range(1, n+1):
        for _ in range(x):
            visited[x] = True
        l.append(x)
        back()
        l.pop()
        visited[x] = False
                        
back()
