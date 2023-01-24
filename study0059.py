ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
gain = 0
for x in ohlc[1:]:
    gain += x[3] - x[0]
print(gain)
