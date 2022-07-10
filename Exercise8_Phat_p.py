
print("Please login first")
user = input("Username : ")
pasw = input("Password : ")
if user == "admin" and pasw == "admin":
    print("---- Welcome to Phat's shop ----")
    print("--------------------------------")
    print("Please select fruit from below and input amount to summarize your bill")
    print("1 - Durian (180/kg)")
    print("2 - Mangosteen (25/kg")
    print("3 - Apple (19/ea)")
    print("4 - Banana (20/ea)")
    print("--------------------------------")
    user_sel = int(input("Select your fruit : "))
    if user_sel == 1:
        price = 180
        print("You select Durian (180/kg)")
    elif user_sel == 2:
        price = 25
        print("You select Mangosteen (25/kg)")
    elif user_sel == 3:
        price = 19
        print("You select Apple (19/ea)")
    elif user_sel == 4:
        price = 20
        print("You select Banana (20/ea)")
    else:
        print("Error select, program will close")
    if price > 0:
        print("--------------------------------")
        amnt = int(input("Please input your amount to buy : "))
        print("--------------------------------")
        print("Your total price is", price * amnt,"THB")
        print("-------    Thank you    -------")
        print("--------------------------------")