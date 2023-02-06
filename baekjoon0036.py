n = input()
l1 = input().split()
l2 = []
for x in l1:
    l2.append(int(x))
l2.sort()
print(l2[0], l2[-1])
