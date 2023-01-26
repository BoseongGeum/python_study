import datetime

n = datetime.datetime.now()

for d in range(5, 0, -1):
    delta = datetime.timedelta(days=d)
    print(n - delta)
