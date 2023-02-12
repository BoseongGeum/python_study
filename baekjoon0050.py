import sys
import collections

word = list(sys.stdin.readline().rstrip().upper())
co = collections.Counter(word)
li = [k for k,v in co.most_common() if co.most_common(1)[0][1] == v]
if len(li) == 1:
    print(li[0])
else:
    print("?")
