l = []
for x in range(5):
    l.append(int(input()))
print(sum(l)//5, sorted(l)[2], sep='\n')
