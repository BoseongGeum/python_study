f = open("C:/Users/K34M/Desktop/매수종목2.txt", encoding="utf-8")
lines = f.readlines()

stocks = {}
for l in lines:
    l = l.strip()
    a, b = l.split()
    stocks[a] = b

print(stocks)

f.close()
