import random

dice = input("vill du slå tärning?")
number = random.randrange(1, 7)
while dice == "ja":
    number = random.randrange(1, 7)
    print(number)
    dice2 = input("vill du slå tärning igen?")
   




