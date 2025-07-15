# Restaurant Tip Splitter

bill_amount = float(input("Enter your total bill amount (₹): "))
tip_percent = float(input("Enter tip percentage (10 to 50): "))
num_friends = int(input("Enter number of friends to split the bill: "))

if tip_percent < 10 or tip_percent > 50:
    print("Tip percentage must be between 10 and 50.")
else:
    tip_amount = (tip_percent / 100) * bill_amount
    total_amount = bill_amount + tip_amount
    each_person_amount = total_amount / num_friends

    print("\n--- Bill Summary ---")
    print(f"Original Bill: ₹{bill_amount:.2f}")
    print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
    print(f"Total Bill (with tip): ₹{total_amount:.2f}")
    print(f"Each Friend Pays ({num_friends} people): ₹{each_person_amount:.2f}")
