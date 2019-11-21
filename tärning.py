import random
import time

def dicee():
    return random.randrange(1, 7)

list_of_throws = []

dice = input("vill du slå tärning?")
time.sleep(1)
while dice == "ja":
    print(dicee())
    list_of_throws.append(dicethrow())
    dice2 = input("vill du slå tärning igen?")
    time.sleep(1)
    if dice2 == ("quit"):
        quit()
    elif dice == "mean":
        print(float(mean_of_throws))    

def sum_of_throws(list_of_throws):
    result = 0
    for x in list_of_throws:
        result = result + x
    return result
 
def mean_of_throws(list_of_throws):
    result = 0 
    for x in list_of_throws:
        result = result + x
    return result / len(list_of_throws)

   




   




