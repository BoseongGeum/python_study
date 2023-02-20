a, b = map(int, input().split())
l = sorted(list(map(int, input().split())))
nl = []
breakout = False
for x in l:
    for y in l:
        if x < y:
            for z in l:
                if y < z:
                    s = x + y + z
                    if s == b:
                        nl.append(s)
                        breakout = True
                        break
                    elif s < b:
                        nl.append(s)
        if breakout == True:
            break
    if breakout == True:
        break

print(max(nl))
