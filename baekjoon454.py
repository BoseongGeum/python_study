import sys
input = sys.stdin.readline

months = [4, 6, 9, 11]
days = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
day, month = map(int, input().split())

sumDays = 0
for cur in range(1, month):
    if cur in months:
        sumDays += 30
    elif cur == 2:
        sumDays += 28
    else:
        sumDays += 31

sumDays += day
rest = sumDays % 7

print(days[rest])
