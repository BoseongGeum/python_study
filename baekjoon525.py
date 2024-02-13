import sys
input = sys.stdin.readline

s = ''
while True:
    try:
        s += input().strip()
    except:
        break
print(sum(map(int, s.split(','))))
