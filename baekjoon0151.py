import sys
input = sys.stdin.readline

n = int(input())
distance = [0] + list(map(int, input().split()))
price = list(map(int, input().split()))
cur_price = price[0]
price_sum = 0

for x in range(1, n):
    price_sum += distance[x] * cur_price
    
    if price[x] <= cur_price:
        cur_price = price[x]

print(price_sum)
