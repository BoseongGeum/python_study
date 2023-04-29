import sys
input = sys.stdin.readline

n = int(input())
m = [list(map(int, input().split()))  for _ in range(n)]

class Tornado:

    def __init__(self, n, m, d):
        self.x = n//2
        self.y = n//2
        self.n = n
        self.m = m
        self.d = d

    def distance(self):
        dis = []
        for i in range(1, self.n):
            dis.extend([i, i])
        dis.append(self.n - 1)
        return dis

    def amount(self):
        return self.m[self.x][self.y]

    def move(self):
        for i in self.distance():
            for _ in range(i):
                self.sandmove()
                if d % 4 == 0:
                    self.y -= 1
                elif d % 4 == 1:
                    self.x += 1
                elif d % 4 == 2:
                    self.y += 1
                elif d % 4 == 3:
                    self.x -= 1
            d += 1
    
    def sandmove(self):
        x = self.x
        y = self.y
        a = self.amount()
        
        try:
            if self.d % 4 == 0:
                self.m[x][y-1] += a * 0.55
                self.m[x][y-2] += a * 0.05
                self.m[x+2][y] += a * 0.02
                self.m[x-2][y] += a * 0.02
                self.m[x+1][y-1] += a * 0.1
                self.m[x-1][y-1] += a * 0.1
                self.m[x+1][y] += a * 0.07
                self.m[x-1][y] += a * 0.07
                self.m[x+1][y+1] += a * 0.01
                self.m[x-1][y+1] += a * 0.01

            elif self.d % 4 == 1:
                self.m[x-1][y] += a * 0.55
                self.m[x-2][y] += a * 0.05
                self.m[x][y+2] += a * 0.02
                self.m[x][y-2] += a * 0.02
                self.m[x-1][y+1] += a * 0.1
                self.m[x-1][y-1] += a * 0.1
                self.m[x][y+1] += a * 0.07
                self.m[x][y-1] += a * 0.07
                self.m[x+1][y+1] += a * 0.01
                self.m[x+1][y-1] += a * 0.01

            elif self.d % 4 == 2:
                self.m[x][y+1] += a * 0.55
                self.m[x][y+2] += a * 0.05
                self.m[x+2][y] += a * 0.02
                self.m[x-2][y] += a * 0.02
                self.m[x+1][y+1] += a * 0.1
                self.m[x-1][y+1] += a * 0.1
                self.m[x+1][y] += a * 0.07
                self.m[x-1][y] += a * 0.07
                self.m[x+1][y-1] += a * 0.01
                self.m[x-1][y-1] += a * 0.01

            elif self.d % 4 == 3:
                self.m[x+1][y] += a * 0.55
                self.m[x+2][y] += a * 0.05
                self.m[x][y+2] += a * 0.02
                self.m[x][y-2] += a * 0.02
                self.m[x+1][y+1] += a * 0.1
                self.m[x+1][y-1] += a * 0.1
                self.m[x][y+1] += a * 0.07
                self.m[x][y-1] += a * 0.07
                self.m[x-1][y+1] += a * 0.01
                self.m[x-1][y-1] += a * 0.01

        except:
            pass
            
    
tor = Tornado(n, m, 0)
tor.move()
