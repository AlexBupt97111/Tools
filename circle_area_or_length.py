import math
r = float(input("Input radius of circle: "))

def getLength(r):
    p = 2 * math.pi * r
    print("Length of circle is", round(p, 2), "cm.")
    
def getArea(r):
    a = math.pi * (r**2)
    print("Area of circle is", round(a, 2), "sq.cm.")

a = input("Input L(for length) or A(for area): ")
if a == "L":
    getLength(r)
elif a == "A":
    getArea(r)   
else:
    print("Mistake. Input L or A. ")
    
###############

import math

class Circle:
    r = float(input("Input radius of circle: "))
    p = input("Input L(for length) or A(for area): ")
  
    def getLength(r):
        a = math.pi * (r**2)
        print(round(a, 2))

    def getPerimeter(r):
        p = 2 * math.pi * r
        print(round(p, 2))
      
    if p == "L":
        getLength(r)
    elif p == "A":
        getArea(r)   
    else:
        print("Mistake. Input P or A. ")
      
c = Circle()

