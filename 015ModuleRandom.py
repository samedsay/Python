# Importing random below:
import random

# Creating random_list below:
random_list =[]

# Creating randomer_number below:
for i in range(101):
  random_list.append(random.randint(1,101))

# Printing randomer_number below:
randomer_number = random.choice(random_list)
print(randomer_number)
