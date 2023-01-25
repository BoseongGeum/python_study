def print_max(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > b and c > a:
        print(c)

def EXprint_max(a, b, c):
    max_val = 0
    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    print(max_val)

print_max(1, 2, 3)
EXprint_max(1, 2, 3)
