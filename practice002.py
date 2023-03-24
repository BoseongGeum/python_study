n = int(input())
l = list(map(int, input().split()))

def mergesort(l):

    if len(l) < 2:
        return l
    
    mid = len(l) // 2
    l1 = mergesort(l[:mid])
    l2 = mergesort(l[mid:])
    
    i = j = 0
    l3 = []
    while i < len(l1) and j < len(l2):
            
        if l1[i] > l2[j]:
            l3.append(l2[j])
            j += 1
                
        else:
            l3.append(l1[i])
            i += 1

    l3 += l1[i:]
    l3 += l2[j:]

    return l3

print(mergesort(l))
