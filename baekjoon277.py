import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tl = list(map(int, input().split()))

c = 0
ul = set()
for i in range(k):
    if tl[i] in ul:
        continue
    
    if len(ul) >= n:
        t = []
        for j in range(i+1, k):
            if len(t) == len(ul):
                break
            if (tl[j] in ul) and (tl[j] not in t):
                t.append(tl[j])
        if len(t) == len(ul):
            ul.remove(t[-1])
        else:
            s = ul - set(t)
            ul.remove(s.pop())
        c += 1
    ul.add(tl[i])

print(c)
