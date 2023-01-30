class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
              print(f'이름: {self.name} 나이: {self.age} 성별: {self.sex}')

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print('나의 죽음을 적에게 알리지 마라')

areum = Human('모름','모름','불명')
areum.setInfo('아름','25','여자')
areum.who()
del areum
