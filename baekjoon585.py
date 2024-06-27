import sys
input = sys.stdin.readline

channels = []

n = int(input())
for _ in range(n):
    channels.append(input().rstrip())

result = ''
i = 0

while channels[i] != 'KBS1':
    i += 1
    result += '1'

while i != 0:
    temp = channels[i]
    channels[i] = channels[i-1]
    channels[i-1] = temp
    i -= 1
    result += '4'

while channels[i] != 'KBS2':
    i += 1
    result += '1'

while i != 1:
    temp = channels[i]
    channels[i] = channels[i-1]
    channels[i-1] = temp
    i -= 1
    result += '4'

print(result)
