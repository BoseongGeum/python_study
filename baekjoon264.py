import sys
input = sys.stdin.readline          

r, c = map(int, input().split())
m = []
for _ in range(r):
    m.append(list(input().rstrip()))

l = 0
for i in range(r):
    for j in range(1, c):
        if i != 0 and m[i-1][j] == '.':
            i -= 1
            m[i][j] = 'x'
        elif m[i][j] == '.':
            m[i][j] = 'x'
        elif i != r-1 and m[i+1][j] == '.':
            i += 1
            m[i][j] = 'x'
        else:
            break
        if j == c-1:
            l += 1

print(l)
