per = ["10.31", "", "8.00"]
per2 = []
for i in per:
    try:
        per2.append(float(i))
    except:
        per2.append(0)

print(per2)
