from numpy import * 

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
c = []

def strassen(n, a, b, c):

    a11 = array([[a[x][y] for y in range(n//2)] for x in range(n//2)])
    a12 = array([[a[x][y] for y in range(n//2, n)] for x in range(n//2)])
    a21 = array([[a[x][y] for y in range(n//2)] for x in range(n//2, n)])
    a22 = array([[a[x][y] for y in range(n//2, n)] for x in range(n//2, n)])
    
    b11 = array([[b[x][y] for y in range(n//2)] for x in range(n//2)])
    b12 = array([[b[x][y] for y in range(n//2, n)] for x in range(n//2)])
    b21 = array([[b[x][y] for y in range(n//2)] for x in range(n//2, n)])
    b22 = array([[b[x][y] for y in range(n//2, n)] for x in range(n//2, n)])
    
    if n <= 2:
        c = array(a) @ array(b)

    else:
        m1 = m2 = m3 = m4 = m5 = m6 = m7 = array([])
        
        m1 = strassen(n//2, (a11 + a22), b11 + b22, m1)
        m2 = strassen(n//2, (a21 + a22), b11, m2)
        m3 = strassen(n//2, a11, (b12 - b22), m3)
        m4 = strassen(n//2, a22, (b21 - b11), m4)
        m5 = strassen(n//2, (a11 + a12), b22, m5)
        m6 = strassen(n//2, (a21 - a11), (b11 + b12), m6)
        m7 = strassen(n//2, (a12 - a22), (b21 + b22), m7)

        c = vstack([hstack([m1 + m4 - m5 + m7, m3 + m5]), hstack([m2 + m4, m1 + m3 - m2 + m6])])

    return c

print(array(a) + array(b))
c = strassen(n, a, b, c)
print(c)
