import random as rd
print("Welcome to rock paper scissors\n You will be facing an AI\nGoodluck!")
i=""
AI=["Rock","Paper","Scissors"]
while i!="end":
    print("ROCK,PAPER,SCISSORS")
    pl=int(input("PLease input a number (0=Rock,1=Paper, 2=Scissors)"))
    s=rd.choice(AI)
    if pl==0:
        e="Rock"
        print("You selected rock")
        print(f"Your opponent choosed {s}")
        if s=="Rock":
            print("It's a tie!")
        elif s=="Paper":
            print("You lose!")
        else:
            print("You win! CONGRATULATIONS")
            i="end"
    elif pl==1:
        e="Paper"
        print("You selected paper")
        print(f"Your opponent choosed {s}")
        if s=="Paper":
            print("It's a tie!")
        elif s=="Scissors":
            print("You lose!")
        else:
            print("You win! CONGRATULATIONS")
            i="end"
    elif pl==2:
        e="Scissors"
        print("You selected scissors")
        print(f"Your opponent choosed {s}")
        if s=="Scissors":
            print("It's a tie!")
        elif s=="Rock":
            print("You lose!")
        else:
            print("You win! CONGRATULATIONS")
            i="end"
    else:
        print("Input invalid!")


