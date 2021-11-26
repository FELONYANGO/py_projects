class mammal:
   def walk(self):
       print("i can move")


class canivore(mammal):
    pass


class omnivore(mammal):
    pass


dogie =canivore()
dogie.walk

pussy=omnivore()
pussy.walk