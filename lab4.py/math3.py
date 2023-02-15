from math import tan,pi
n_s=int(input("Input number of sides:"))
l_s=float(input("Input the length of a side:"))
a_polygon=n_s*(l_s**2) / (4*tan(pi/n_s))
print("The area of the polygon is:", a_polygon)

