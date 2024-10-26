from ASCII import logo
import random
weapons = ["Sword", "Gun", "Virus"]
shields = ["Armour", "Anti gun", "Antibiotic"]

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = 0
        self.shield = 0

    def damage(self):
        points = random.randint(10, 35)
        self.health -= points

    def selectWeapon(self):
        choice = int(input("Choose your weapon 1-Sword, 2-Gun or 3-Virus:  "))
        self.weapon = choice - 1



    def selectShield(self):
        choice = int(input("Choose your shield 1-Armour, 2-Anti gun or 3-Antibiotic:  "))
        self.shield = choice - 1


# Child class of player with override methods for weapon
# and shield selection
class AiPlayer(Player):
    def __init__(self,name):
        super().__init__(name)

    def selectWeapon(self):
        choice = random.randint(1, 3)
        self.weapon = choice - 1

    def selectShield(self):
        choice = random.randint(1, 3)
        self.shield = choice - 1

class Game:
    def __init__(self):
        self.gameOver = False
        self.round = 0

    def newRound(self):
        self.round += 1
        print("\n***   Round: %d   ***\n" %(self.round))

    # Check if either or both Players is below zero health
    def checkWin(self, player, opponent):
        if player.health < 1 and opponent.health > 0:
            self.gameOver = True
            print("You Lose *you fell desperate and your soul slowly go to the unknown(VOID)*")
        elif opponent.health < 1 and player.health > 0:
            self.gameOver = True
            print("CONGRATS You Win *your enemy fell to the unknown(VOID)*")
        elif player.health < 1 and ai.health < 1:
            self.gameOver = True
            print("*** Draw ***")


    def displayResult(self, player, opponent):
            print("%s used a %s, %s used a %s Shield\n" %(player.name, weapons[player.weapon], opponent.name, shields[opponent.shield]))
            print("%s caused damage to %s\n" %(player.name, opponent.name))

    def takeTurn(self, player, opponent):

        # Decision Array
        #
        #           Armour|  Magic |  Water
        #           ______|________|_______
        # Sword:    False |  True  |  True
        # Spell:    True  |  False |  True
        # Fire :    True  |  True  |  False

        decisionArray = [[False, True, True], [True, False, True], [True, True, False]]
        if decisionArray[player.weapon][opponent.shield]:
            opponent.damage()
            currentGame.displayResult(player, opponent)
        else:
            print("\n%s used a %s, %s used a %s Shield" %(player.name, weapons[player.weapon], opponent.name, shields[opponent.shield]))
            print("%s blocked %s's attack - No Damage" %(opponent.name, player.name))


print(logo)
print("WELCOME TO RAMPAGE A BATTLE TURN BASED GAME\n\nBY:A312AM\n\nIN THIS GAME U CAN PLAY A BATTLE WITH YOUR ENEMY\n*HOW TO PLAY*\n\nCHOOSE YOUR WEAPON AND SHIELD IF YOUR WEAPON NOT BE COUNTER BY THE ENEMY SHIELD YOU WILL DEAL A DAMAGE,AND VICE VERSA,AND WHEN YOUR ENEMY HP = 0 YOU WIN,AND VICE VERSA  ")

# Setup Game Objects
currentGame = Game()
human = Player (input("choose your name : "))
ai = AiPlayer(input("choose your enemy name : "))

players = [human, ai]

# Main Game Loop
while not currentGame.gameOver:
    for player in players:
        player.selectWeapon()
        player.selectShield()
    currentGame.newRound()
    currentGame.takeTurn(human, ai)
    currentGame.takeTurn(ai, human)
    print("%s's health = %d" %(human.name, human.health))
    print("%s's health = %d" %(ai.name, ai.health))
    currentGame.checkWin(human, ai)
