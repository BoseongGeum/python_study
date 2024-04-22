import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    t = input().rstrip()
    three = {'TTT':0, 'TTH':0, 'THT':0, 'THH':0, 'HTT':0, 'HTH':0, 'HHT':0, 'HHH':0}
    for i in range(38):
            three[t[i:i+3]] += 1

    print(*three.values())
