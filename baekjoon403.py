import sys
input = sys.stdin.readline

s = input().rstrip()
k = input().rstrip()

s = s.replace("0", "")
s = s.replace("1", "")
s = s.replace("2", "")
s = s.replace("3", "")
s = s.replace("4", "")
s = s.replace("5", "")
s = s.replace("6", "")
s = s.replace("7", "")
s = s.replace("8", "")
s = s.replace("9", "")

if k in s:
    print(1)
else:
    print(0)
