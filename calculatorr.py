a = float(input("first number is:"))
b = float(input("second number is:"))
print("choose your operation ")
print("1.addition(+)")
print("2.multiply(*)")
print("3.divide(/)")
print("4.subtraction (-)")
choice= input("choose your number (1/2/3/4):")
if choice == "1":
    print("result",a + b)
elif  choice == "2":
    print("result",a * b)  
elif  choice =="3":
    print("result",a/b)
elif choice == "4":
    print("result", a-b)
else:
    print("invalid choice")       