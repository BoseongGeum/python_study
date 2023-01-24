apart = [ [101, 102], [201, 202], [301, 302] ]
for x in apart[::-1]:
    for y in x[::-1]:
        print(y, "호")
