import math

a = float(input("Enter the length of the first side (a):"))
b = float(input("Enter the length of the first side (b):"))

c = math.sqrt(a**2 + b ** 2)

print(f"The Length of the hypotenuse is {c:2f}")
