quantity = int(input("How many products did you sell? "))
price = float(input("How much does each product cost? "))

total_sales = quantity * price
print(f"The total sales amount is ${total_sales:.2f}")

commission_percent = float(input("What is your commission percent? "))

commission_amount = commission_percent * total_sales / 100
print(f"You earned ${commission_amount:.2f} in commission")

if total_sales > 1000:
    print("Congratulations! You earned the bonus!")
    print("Keep it up!")

print("Have a good day")
