ai = input()
if int(ai) < 10:
    ai = "0"+ai
b, c = map(int, list(ai))
s = str(b + c)
e = str(c)
count = 1
  
while True: 
    if int(s) < 10:
        s = "0"+s
    d = list(s)[1]
    a = str(e) + d
    if (str(b) + str(c) == a) or (a == ai):
        break
    else:
        count += 1
    f, e = map(int, list(a))
    s = str(e + f)

print(count)
