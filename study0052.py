data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for x in data:
    for y in x:
        y = y * 1.00014
        result.append(y)
print(result)
