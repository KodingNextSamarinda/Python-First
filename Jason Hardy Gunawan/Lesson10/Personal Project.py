hutan = """..."""
characterA = """..."""



charData = [hutan, characterA]


plotOne = ["Hello what a beutiful day, it's my first time to be here. ", "Hello sir, where would you recommend me to go?", "I would like to rcommend you to go to our beutiful jungle!"]\


continueGame = ""



def plotTwo():
    print("this is part two")


for index, story in enumerate(plotOne):
    print(story)
    if index == 2:
        continueGame = input("Type yes to continue:")
        if continueGame == "yes":
            plotTwo()
        else:
            print("Oke good bye!!!!")
            break

    else:
        nextText = input("Enter to continue...")















