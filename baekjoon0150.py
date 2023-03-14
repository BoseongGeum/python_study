import sys
input = sys.stdin.readline

sik1, *sik2 = input().split('-')
sik1_sum = sum(map(int, sik1.split('+')))
sik2_sum = 0

for x in sik2:
    sik2_sum += sum(map(int, x.split('+')))

print(sik1_sum - sik2_sum)
