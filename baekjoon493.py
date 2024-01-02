import sys
input = sys.stdin.readline

colors = [('black', 1), ('brown', 10), ('red', 100), ('orange', 1000), ('yellow', 10000), ('green', 100000), ('blue', 1000000), ('violet', 10000000), ('grey', 100000000), ('white', 1000000000)]

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

for i in range(len(colors)):
    if a == colors[i][0]:
        firstValue = i * 10
    if b == colors[i][0]:
        secondValue = i
    if c == colors[i][0]:
        lastValue = colors[i][1]

print((firstValue + secondValue) * lastValue)
