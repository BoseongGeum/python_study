import sys

while True:
    try:
        a, b = map(int, input().split())
        result = round(a/b, 2)
        print(f"{result:.2f}")
    except:
        break
