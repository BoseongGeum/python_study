import sys
input = sys.stdin.readline          

n = int(input())

change = 1000 - n
c = 0
cur = change//500
change -= cur * 500
c += cur
cur = change//100
change -= cur * 100
c += cur
cur = change//50
change -= cur * 50
c += cur
cur = change//10
change -= cur * 10
c += cur
cur = change//5
change -= cur * 5
c += cur + change

print(c)
