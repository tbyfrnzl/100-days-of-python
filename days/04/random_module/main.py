import random
# Import PI module to use variable
import pi_module

random_integer = random.randint(100, 200)
print(random_integer)

random_float = random.random()
print(random_float)

random_float_range = random.uniform(1, 5)
print(random_float_range)

print(pi_module.pi)
