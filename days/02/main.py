# Tip Calculator

# Greeting
print("Welcome to the tip calculator!")

# Ask for total bill
total_bill = float(input("How much was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12 or 15? "))

tip_percentage = tip / 100

people = int(input("How many people want to split the bill? "))

total_bill_with_tip = total_bill + (total_bill * tip_percentage)

price_per_person = total_bill_with_tip / people

formatted_price = "{:.2f}".format(price_per_person)

print(f"According to the given numbers, each person should pay ${formatted_price}.")
