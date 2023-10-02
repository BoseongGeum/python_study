import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '#':
        break

    count = 0
    for a in s[2:]:
        if a == s[0] or a == s[0].upper():
            count += 1

    print(s[0], count)
