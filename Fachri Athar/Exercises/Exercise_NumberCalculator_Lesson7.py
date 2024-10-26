num=[]
i=input("enter your number:")

while i!="done":
    print("Your number has been added")
    j=int(i)
    num.append(j)
    print (num)

    i = input("enter your number:")
total=0
for e in num:
       total = total + e
print(f"The answer is {total}")