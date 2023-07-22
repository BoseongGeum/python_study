import sys
input = sys.stdin.readline

l = [0, 0]
for i in range(2):
    for j in reversed(range(1, 4)):
        n = int(input())
        l[i] += n * j
    

if l[0] > l[1]:
    print('A')

elif l[0] < l[1]:
    print('B')

else:
    print('T')
