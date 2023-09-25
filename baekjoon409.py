import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    string = input().rstrip()
    print(f"{i+1}. {string}")
