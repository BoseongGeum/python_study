while True:
    try:
        s = input()
        upp = 0
        low = 0
        sp = 0
        num = 0
        for c in s:
            ch = ord(c)
            if ch == 32:
                sp += 1
            elif 48 <= ch <= 57:
                num += 1
            elif 65 <= ch <= 90:
                upp += 1
            elif 97 <= ch <= 122:
                low += 1
        print(low, upp, num, sp)
        
    except EOFError:
        break
