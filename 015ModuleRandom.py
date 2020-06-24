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

# Showing data on diagram
from matplotlib import pyplot as plt

numbers_a = range(1,13)
numbers_b = random.sample(range(1, 100), 12)
plt.plot(numbers_a,numbers_b)
plt.show()
