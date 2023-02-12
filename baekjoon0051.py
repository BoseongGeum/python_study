import sys

word = sys.stdin.readline().strip().split(' ')
if '' in word:
    print(0)
else:
    print(len(word))
