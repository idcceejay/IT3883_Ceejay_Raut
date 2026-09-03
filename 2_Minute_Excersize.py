import math

pi = math.pi
user_input = float(input("Enter a Radius: "))
circle = pi * (user_input ** 2)
print(f"The area of the circle is: {circle}")

sphere = 4/3 * pi * (user_input ** 3)
print(f"The volume of the sphere is: {sphere}") 

solution_3 = 2 * pi * user_input