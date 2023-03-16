import sys
input = sys.stdin.readline

n = int(input())

def hanoi(n, cur_tow, mid_tow, fin_tow):

    if n == 1:
        return print(cur_tow, fin_tow)

    hanoi(n - 1, cur_tow, fin_tow, mid_tow)
          
    print(cur_tow, fin_tow)

    hanoi(n - 1, mid_tow, cur_tow, fin_tow)

print(2**n - 1)
hanoi(n, 1, 2, 3)
