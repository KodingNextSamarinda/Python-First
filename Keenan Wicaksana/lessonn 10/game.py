from art import graphic
import random
print(graphic)

print("GAME"
      "\nyou are trapped in a maze go find treasure")
def foward():
    print ("you moved foward")
def backward():
    print ("you moved backward")
def left():
     print("you moved left")
def right():
     print("you moved right")
def item():
         print("you got stuff")

key = input("what key w/a/s/d:")
if key == "w":
    foward()
elif key == "s":
    backward()
elif key == "a":
    left()
elif key == "d":
    right()
elif key == "e":
    item()


path=["w", "w", "d", "d", "s", "a", "w"]
