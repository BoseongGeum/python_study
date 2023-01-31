class Stock:
    def __init__(self, name, code, PER, PBR, 배당수익률):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.배당수익률 = 배당수익률
 
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, PER):
        self.PER = PER
        
    def set_pbr(self, PBR):
        self.PBR = PBR
        
    def set_dividend(self, 배당수익률):
        self.배당수익률 = 배당수익률

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

a = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
a.set_per(12.75)
print(a.PER, a.PBR, a.배당수익률)
