def floyd(n, w, d):
    w = [[],[],[]] # 가중치는 이차원 배열
    d = [[],[],[]]

    for k in range(n):
        for j in range(n):
            for i in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
