a = int(input("enter male age :"))
b = int(input("enter female age :"))


if a >= 21:
 print("male is eligible for marriage")
else:
    print("male is not eligible for marriage")
    
    if b >=18:
        print("female is eligible for marriage")
    else:
        print("female is not eligible for marriage")
        
    if a>= 21 and b>= 18:
     print(" the match is perfect")


