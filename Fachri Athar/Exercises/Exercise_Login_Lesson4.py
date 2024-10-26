User=input("Masukkan username ")
Password=input("Masukkan password ")
if Password=="123456" and User=="Ninja987654":
    print("Selamat Datang")
elif Password!="123456" and User=="Ninja987654":
    print("Password salah")
elif Password=="123456" and User!="Ninja987654":
    print("Username salah")
else:
    print("Password dan username salah")