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
    
    def div(self):
        return self.first / self.second

x = int(input("Please enter first number : "))
y = int(input("Please enter second number : "))
a = FourCal(x, y)

print("합은 ", a.add())
print("차는 ", a.sub())
print("곱은 ", a.mul())
print("몫은 ", a.div())