from title  import abcde
import random


#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter3=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter4=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter5=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
#....

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5
password = shuffle(password)

#Ouput

ulang = False
a = input ("Do you want to print it?")
while ulang != True and a == "Yes" or a == "yes":

    print("This is your password: ")
    print(password)

    a = input("Do you want to print it again ?")

    if a == "No" or a == "no":
        print("Okay maybe next time")
        ulang = True


# ulang = True
#
# t = input ("Please enter time in seconds: ")
#
# countdown (int(t))
#
# c = input("try?")
#
# while ulang != False:
#     t = input("Please enter time in seconds: ")
#
#     countdown (int(t))
#     c = input ("try?")
#     if c == "no" :
#         ulang = False
#
