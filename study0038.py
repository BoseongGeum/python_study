my_list = [100, 200, 400, 800, 1000, 1300]
for x in range(2, len(my_list)):
    print((my_list[x - 2] + my_list[x] + my_list[x - 1])/3)
