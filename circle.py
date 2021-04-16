def size_of_circle(a):
    return (a ** 2) * 3.14

def circumference_of_circle(a):
    return 2 * a * 3.14

print("please enter the radius of circle you want")
a = float(input())

print(size_of_circle(a))
print(circumference_of_circle(a))