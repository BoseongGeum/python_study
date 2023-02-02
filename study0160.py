per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("실수화 성공")
    finally:
        print("코딩 재밌다")
