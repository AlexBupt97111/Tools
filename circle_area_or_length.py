import math
try:
    class Circle:
        r = float(input("Input radius of circle: "))
        b = input("Input L(for length) or A(for area): ")
  
        def getLength(r):
            l = 2 * math.pi * r
            print("Length of circle is", round(l, 2), "cm.") 
     
        def getArea(r):
            a = math.pi * (r**2)
            print("Area of circle is", round(a, 2), "sq.cm.")
            
        if b == "L":
            getLength(r)
        elif b == "A":
            getArea(r)   
        else:
            print("Mistake. Input L or A. ")  
            
    c = Circle()    
except ValueError:
    print("Input only digits, not letters or other symbols.Check please and try it again")

