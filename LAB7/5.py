volume_of_cone = lambda r, h: (1/3) * 3.14 * r**2 * h

r = float(input("Enter radius: "))
h = float(input("Enter height: "))
volume = volume_of_cone(r, h)
print("Volume of cone:", volume)
