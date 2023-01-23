리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for x in 리스트:
    a,b = x.split(".")
    if b == "h" or b == "c":
        print(x)
