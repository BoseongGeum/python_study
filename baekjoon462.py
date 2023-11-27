import sys
input = sys.stdin.readline

string = input().rstrip()

countJ = 0
countI = 0
for i in range(len(string)-2):
    if string[i:i+3] == 'JOI':
        countJ += 1
    elif string[i:i+3] == 'IOI':
        countI += 1

print(countJ)
print(countI)
