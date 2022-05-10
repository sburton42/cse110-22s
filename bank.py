# find out the amount they have in their account
balance = float(input("How much is in your account? "))

additional_purchase = "yes"
while additional_purchase.lower() == "yes":
    # ask them how much the charge is
    charge = float(input("What is the amount of the charge? "))

    # calculate the difference between what they have and what they want
    difference = balance - charge
    print(f"The difference is: {difference}")

    # check if the difference is negative
    while difference < 0:
        # if so, say card declined
        print("Card Declined.")

        # try another charge amount
        charge = float(input("Please try another charge amount: "))
        difference = balance - charge

    # update the balance
    balance = balance - charge
    # I could have written balance -= charge

    # display the remaining balance
    print(f"Your remaining balance is ${balance:.2f}")

    additional_purchase = input("Would you like to make another purchase? ")
    