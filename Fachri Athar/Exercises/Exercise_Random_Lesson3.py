import random
Num = random.randrange(1 , 10)
print("Hmmmmmm i am thinking a number between 1 to 10")
answer =int(input ("What is the number i thinking? "))
if answer==Num:
    print("That answer is correct!")
else:
    print("That answer is incorrect")
    print(f"The correct answer is {Num}")
