def print_5xn(string):
    for x in range((len(string) // 5) + 1):
        print(string[x * 5 : x * 5 + 5])

print_5xn("아이엠어보이유알어걸")
