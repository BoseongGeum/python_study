def pickup_even(x):
    List = []
    for a in x:
        if a % 2 == 0:
            List.append(a)
    return List

pickup_even([3, 4, 5, 6, 7, 8])
