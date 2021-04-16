class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def set_data(self, first, second):
        self.first = first
        self.second = second       

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second
    
    
class FourCal_div(FourCal):
    def div(self):
        return self.first / self.second


div_data = FourCal_div(4, 2)
a = div_data.div()
print(a)
b = div_data.add()
print(b)