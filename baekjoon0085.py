def recursion(s, l, r):
    if l >= r:
        print(1, l+1)
    elif s[l] != s[r]:
        print(0, l+1)
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())
for x in range(n):
    s = input()
    isPalindrome(s)
