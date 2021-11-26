import random
from pathlib import Path


class Dice:
    def roll(self):
       first= random.randint(1,6)
       secend= random.randint(1,6)
       
       return (first,secend)

    
dice1=Dice()
print(dice1.roll())

path = Path()
for file in path.glob("*.py"):
    print(file)
