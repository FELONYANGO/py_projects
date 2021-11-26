import random
from shipping import calculate_shipping

calculate_shipping()

for i in range (3):
   print(random.random())
   print(random.randint(1,100))

group_8=["fela","felix","liz","calvince"]
leader=random.choice(group_8)
print(leader)


for i in range(1,3):
    for z in range(1,3):
        print(f"{i,z}")