wo = list(input())
cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
co = 0

for x in range(len(wo) - 1):
    if wo[x] + wo[x + 1] in cr:
        co += 1
for x in range(len(wo) - 2):
    if wo[x] + wo[x + 1] + wo[x + 2] in cr:
        co += 1
print(len(wo) - co)
