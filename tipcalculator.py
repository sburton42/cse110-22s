def calculate_tip(total, tip_percent):
    tip_amount = total * tip_percent / 100
    return tip_amount

def add_tax(subtotal, tax_percent):
    tax_amount = subtotal * tax_percent / 100
    total = subtotal + tax_amount
    return total

total_meal = float(input("What is the price of the meal? "))
tax_total = add_tax(total_meal, 6)
print(f"The total after tax is: ${tax_total:.2f}")

for percent in range(15, 26, 1):
    tip_amount = calculate_tip(tax_total, percent)
    print(f"A {percent}% tip would be: ${tip_amount:.2f}")
