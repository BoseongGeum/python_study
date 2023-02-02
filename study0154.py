f = open("C:/Users/K34M/Desktop/매수종목1.txt", encoding="utf-8")
lines = f.readlines()

codes = []
for l in lines:
    c = l.strip()
    codes.append(c)

print(codes)

f.close()
