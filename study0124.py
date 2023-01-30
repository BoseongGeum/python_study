class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
 
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

st = Stock(None, None)
st.set_name("삼성전자")
st.set_code("005930")
print(st.code)
