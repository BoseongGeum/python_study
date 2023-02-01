import csv

f = open("C:/Users/K34M/Desktop/매수종목.csv", mode="wt", encoding="cp949",
         newline='')
w = csv.writer(f)
w.writerow(["종목명","종목코드","PER"])
w.writerow(["삼성전자","005930","15.59"])
w.writerow(["NAVER","035420","55.82"])
f.close()
