n = int(input())
l = []
for x in range(n):
    l.append(int(input()))
print(*sorted(l), sep='\n')
