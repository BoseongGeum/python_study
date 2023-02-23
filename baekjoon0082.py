x,y,w,h = map(int, input().split())

g1 = w - x
g2 = h - y
print(min([x,y,g1,g2]))
