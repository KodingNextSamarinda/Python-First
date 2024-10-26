import random
num=random.randrange(5,11)
answer=int(input("What is the answer:(Hint: it is more than 5 but less than 10 or equal to 10):"))
if answer==num:
    print("Your answer is correct")
else:
    while answer!=num:
        answer=int(input("Wrong! what is the answer"))
        if answer == num:
            print("Your answer is correct")


