import random

from artist import logo
print(logo)

easy_mode = 10
normal_mode = 7
hard_mode = 5

tebakan_komp = random.randrange (1,100)

def cek_nyawa(nyawa):
    if nyawa > 0:
        print(f"your attempt is {nyawa}")

def checkdifficulity():
    mode = input ("choose mode, 'easy' , 'normal' or 'hard' : ")
    if mode == "easy":
        return easy_mode
    elif mode == "normal":
        return normal_mode
    elif mode == "hard":
        return hard_mode

def perbandinganagka(player, computer):
    if player > computer:
        print("no,you're too high")
    elif player < computer:
        print("no, you're too low")
    elif player == computer:
        print(f"correct answer, I'm guessing number is {computer}")

def show():
    print("Hello player, welcome to 'Guessing the Number' game. I have 1 until 100 number, can you guess the number I think?")
    tingkatan = checkdifficulity()
    guess = 0
    while tingkatan > 0 and guess != tebakan_komp:
        cek_nyawa(tingkatan)
        tingkatan -= 1
        guess = int(input("your guess: "))
        perbandinganagka(player=guess , computer= tebakan_komp)
        if tingkatan == 0:
            print("sorry player, you lose your attempt :( ")


show()
