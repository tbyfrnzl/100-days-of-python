# Not a complete list of american states :)
states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]

# Reading items from a list
print(f"Second state to join the union was {states_of_america[1]}")
print(f"Last state to join the union was {states_of_america[-1]}")

# Changing items in a list
states_of_america[1] = "Pencilvania"

print(f"Second state to join the union was {states_of_america[1]}")

# Add to the end of the list
states_of_america.append("Georgia")

print(states_of_america)

# Add multiple values to the end of the list
states_of_america.extend(["Connecticut", "Massachusetts", "Maryland"])

print(states_of_america)