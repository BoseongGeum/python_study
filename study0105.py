import datetime

n = "2020-05-04"
r = datetime.datetime.strptime(n, "%Y-%m-%d")
print(type(r))
