import math
r = float(input("Input radius of circle: "))

def getArea(r):
    a = math.pi * (r**2)
    print("Area of circle is", round(a, 2), "sq.cm.")

def getLength(r):
    p = 2 * math.pi * r
    print("Length of circle is", round(p, 2), "cm.")

a = input("Input P(for perimeter) or A(for area): ")
if a == "P":
    getLength(r)
elif a == "A":
    getArea(r)   
else:
    print("Mistake. Input P or A. ")
