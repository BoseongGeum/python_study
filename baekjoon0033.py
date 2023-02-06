try:
    a, b = list(input())
except:
    a, b = list("0"+input())

try:
    c, d = list(str(int(a) + int(b)))
except:
    c, d = list("0"+ str(int(a) + int(b)))
count = 1
while b + d == a + b:
    c, d = list(str(int(b) + int(d)))
    count += 1
print(count)
