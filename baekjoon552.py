import sys

i = 0
while True:
    try:
        input().rstrip()
        i += 1
    except:
        break
    
print(i)
