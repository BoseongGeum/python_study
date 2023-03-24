n = int(input())
l = list(map(int, input().split()))

def mergesort(l):
    
    def sort(s, e):
        if e - s < 2:
            return

        mid = (s + e) // 2
        sort(s, mid)
        sort(mid, e)
        
        return merge(s, mid, e)

    def merge(s, mid, e):
        g, h = s, mid
        a = []
        
        while g < mid and h < e:
            if l[g] < l[h]:
                a.append(l[g])
                g += 1
            else:
                a.append(l[h])
                h += 1
                
        while g < mid:
            a.append(l[g])
            g += 1
        while h < e:
            a.append(l[h])
            h += 1

        for i in range(s, e):
            l[i] = a[i - s]
        return l
    
    return sort(0, len(l))

print(mergesort(l))
