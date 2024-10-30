from logo import art
print(art)
print("welcome to the would you rather game!")
print("here are the rules so I'm gonna tell you a question then you answer it")
Answer1 = int(input("now its time to tell you an answer now would you rather get 1 = Rp 100 000 or 2 = a luxury car?"))

if Answer1 == 1:
    print("you get a free burger")
elif Answer1 == 2:
    print("you get an extra of Rp 10 000")
else:
    print("you enter the wrong number")

Answer2 = int(input("Next question would you rather get a 3 = diamond or 4 = gold?"))
if Answer2 == 3:
    print("you get a ticket to Hawaii")
elif Answer2 == 4:
    print("you get a brand new tv")
else:
    print("you enter the wrong number")

Answer3 = int(input("lets do another question would you rather get an 5 = apple or 6 = banana?"))
if Answer3 == 5:
    print("you get a trip to a hotel")
elif Answer3 == 6:
    print("you get a xbox")
else:
    print("you enter the wrong number")

Answer4 = int(input("another question would you rather 7 = see a meteor or 8 = shoot the meteor?"))
if Answer4 == 7:
    print("so you get a bike")
elif Answer4 == 8:
    print("so you survive the meteor")
else:
    print("you enter the wrong number")

Answer5 = int(input("last question would you rather 9 = drink tea or 10 = drink coffee?"))
if Answer5 == 9:
    print("you can be calm now")
elif Answer5 == 10:
    print("you can't be able to sleep now")
else:
    print("you enter the wrong number")

print("thanks for playing")
