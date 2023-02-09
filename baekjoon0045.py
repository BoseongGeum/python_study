n = int(input())
hansu_list = []

for x in range(1,n+1):
    l = list(map(int, list(str(x))))
    if len(l) < 3:
        hansu_list.append(x)
    elif l[2] - l[1] == l[1] - l[0]:
        hansu_list.append(x)
print(len(hansu_list))
