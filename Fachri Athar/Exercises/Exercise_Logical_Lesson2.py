AliceFav=input("Makanan kesukaan Alice: ")
AliceAm=int(input("Jumlah: "))
JohnFav=input("Makanan kesukaan John: ")
JohnAm=int(input("Jumlah: "))
print("Lie Detector")
print(f'Alice: Makanan kesukaanku adalah {AliceFav} atau Aku memiliki {AliceAm} Makanan')
print(AliceFav=="KFC" or AliceAm==7)
print(f'John: Makanan kesukaanku adalah {JohnFav} dan Aku masih memiliki lebih dari 5 makanan')
print(JohnFav=="Mcdonalds" and JohnAm>5)
print("John atau Alice memiliki 10 makanan")
print(JohnAm==10 or AliceAm==10)

