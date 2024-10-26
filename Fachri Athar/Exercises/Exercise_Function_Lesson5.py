import random

def function(name,age):
    print(f"Your name is {name} and your age is {age}")
def max(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"the biggest number is {num1}")
    elif num2 > num1 and num2 > num3:
        print(f"the biggest number is {num2}")
    elif num3 > num1 and num3 > num2:
        print(f"the biggest number is {num3}")
def Num(angka1,angka2):
    jumlah=angka1+angka2
    kurang=angka1-angka2
    kali=angka1*angka2
    return jumlah,kali,kurang
def ganjilgenap(a):
    if a%2==1:
        print(f"{a} is an odd number")
    elif a%2==0:
        print(f"{a} is an even number")
nama=input("Name: ")
umur=int(input("Age:"))
function(nama, umur)
jumlahhuruf=len(nama)
print(f"your name has {jumlahhuruf} character")
ganjilgenap(random.randrange(1,1000))
E=Num(5,4)
print(E)
max(1,5,3)
