def print_mxn(string, n):
    for x in range((len(string) // n) + 1):
        print(string[x * n : x * n + n])

print_mxn("아이엠어보이유알어걸", 3)
