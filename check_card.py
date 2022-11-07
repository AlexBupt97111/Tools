try:
    num = int(input("Input your credit card number, please: "))
    x = [int(a) for a in str(num)]
    if len(x) < 16:
        print("Ups. Are you input all digits? Check please.")
    elif len(x) > 16:
        print("Too long. Somewhat redundant. Check please.")
    else:
        c = x[-4:] 
        b = ''.join(str(a) for a in c) 
        print("**** **** ****", b)
        print("All ok.")    
except ValueError:
    print("Some mistake. Input only digits, not letters or other symbols. Check please, and try it again.")  
