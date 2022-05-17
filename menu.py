order = []

choice = ""

while choice != "4":
    print("Menu:")
    print("1 - Drink")
    print("2 - Sandwich")
    print("3 - Dessert")
    print("4 - Quit")

    choice = input("What would you like to order? ")

    if choice == "1":
        drink = input("What type of drink would you like? ")
        size = input("What size? ")
        #drink_order = size + " " + drink
        drink_order = f"{size.capitalize()} {drink.capitalize()}"
        order.append(drink_order)

    elif choice == "2":
        order.append("Sandwich")
    elif choice == "3":
        order.append("Dessert")

print("The contents of your order are:")
for item in order:
    print(item)




# This is an option to use multi-line strings
# print("""Menu:
# 1 - Drink
# 2 - Sandwich
# 3 - Dessert
# """)
