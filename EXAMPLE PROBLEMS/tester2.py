side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

sides_squared = [side1**2, side2**2, side3**2]

sides_squared.sort()

if sides_squared[0] + sides_squared[1] == sides_squared[2]:
    print("The triangle is a right traiangle.")
else:
    print("The triangle is not a right triangle.")
