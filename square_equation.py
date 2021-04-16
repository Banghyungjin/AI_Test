def root_ex(a, b, c):
    answer1 = (((-1 * b) + ((b ** 2) - (4 * a * c)) ** 0.5 ) / (2 * a))
    answer2 = (((-1 * b) - ((b ** 2) - (4 * a * c)) ** 0.5 ) / (2 * a))
    print(answer1)
    print(answer2)

print("please enter a")
a = int(input())
print("please enter b")
b = int(input())
print("please enter c")
c = int(input())

root_ex(a, b, c)