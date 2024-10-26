Nama1=input("Nama pertama: ")
Num1=int(input(f"Usia {Nama1}="))
Nama2=input("nama kedua: ")
Num2=int(input(f"Usia {Nama2}="))
Nama3=input("Nama ketiga: ")
Num3=int(input(f"Usia {Nama3}:"))
if Num1>Num2 and Num1>Num3:
    print(f"Orang tertua adalah {Nama1} dengan usia {Num1}")
elif Num2>Num1 and Num2>Num3:
    print(f"Orang tertua adalah {Nama2} dengan usia {Num2}")
elif Num3>Num2 and Num3>Num1:
    print(f"Orang tertua adalah {Nama3} dengan usia {Num3}")
else:
    print(f"{Nama1},{Nama2}, dan {Nama3} memiliki usia yang sama yaitu {Num1}")