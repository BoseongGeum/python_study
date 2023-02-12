import sys

co = 0
n = int(input())
for x in range(n):
    al = []
    wo = list(sys.stdin.readline().rstrip())
    for x in range(len(wo) - 1):
        if wo[x] == wo[x + 1]:
            pass
        else:
            if wo[x + 1] in al:
                co += 1
                break
            else:
                al.append(wo[x])
                al.append(wo[x + 1])
print(n - co)
