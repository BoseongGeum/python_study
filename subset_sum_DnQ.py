def DnQ(l, total):

    if len(l) < 2:
        return l
    
    mid = len(l) // 2
    l1 = DnQ(l[:mid], total)
    l2 = DnQ(l[mid:], total)
    
    l3 = l1[:] + l2[:]
    for x in l1:
        for y in l2:
            s = x + y
            if s <= total and s not in l3:
                l3.append(s)
                record[s] = [x, y]

    return l3

total, *l = map(int, input().split())
record = [[] for _ in range(total+1)]

l3 = DnQ(l, total)

def find(i, record):
    if record[i] != []:
        for x in record[i]:
            if x in l:
                print(x, end=' ')
            else:
                find(x, record)
    else:
        print(*record[i])

if total in l3:
    i = total
    find(i, record)
    
else:
    print(-1)
