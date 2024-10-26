print("Halo untuk membuat username ada ketentuan ketentuan berikut:\n1.Lebih dari 3\n2.Kurang dari 10 ")
User=input("User: ")
if len(User)>3 and len(User)<10:
    print(f"Berhasil selamat datang,{User}")
else:
    print("Nama tidak memenuhi syarat")
