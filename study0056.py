ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for x in ohlc[1:]:
    if x[-1] >= x[0]:
        print(x[-1])
