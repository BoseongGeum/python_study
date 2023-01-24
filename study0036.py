my_list = ["가", "나", "다", "라"]
for x in range(1, len(my_list))[::-1]:
    print(my_list[x], my_list[x - 1])
