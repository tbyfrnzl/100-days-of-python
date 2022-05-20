# For loops with lists
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# For loops with range and steps
for num in range(1, 11, 3):
    print(num)

# For loops with range without steps
total = 0
for num in range(1, 101):
    total += num

print(total)