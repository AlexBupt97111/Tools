num = int(input("Input your credit card number, please: "))
x = [int(a) for a in str(num)]
if len(x) < 16:
    print("Too short. Are you input all digits? Check please.")
elif len(x) > 16:
  print("Too long. Somewhat redundant. Check please.")
else:
    c = x[-4:] #last 4 digits
    b = ''.join(str(a) for a in c) #list to str
    print("************",b)
    print("Ok. Choose next action, please")
