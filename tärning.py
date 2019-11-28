import random
import time

list_of_throws = []

def average(numbers):
    return sum(numbers) / len(numbers)

dice = input("vill du slå tärning?")
result = random.randint(1,6)
time.sleep(1)
while dice == "ja":
    result = random.randint(1,6)
    list_of_throws.append(result)
    print(result)
    dice = input("vill du slå tärning igen?")
    time.sleep(1)
else:
    print("ok, ha det så bra") 

print(list_of_throws)
print(average(list_of_throws))       

    
