import secrets
import string
#Mengimport arsci art dari art.py
from art import kelinci
print(kelinci)

# Funcation with parameter untuk membuat password
def create_pw(pw_length=12):
   letters = string.ascii_letters
   digits = string.digits
   special_chars = string.punctuation

   alphabet = letters + digits + special_chars
   pwd = ''
   pw_strong = False

   while not pw_strong:
       pwd = ''
       for i in range(pw_length):
           pwd += ''.join(secrets.choice(alphabet))

       if (any(char in special_chars for char in pwd) and
               sum(char in digits for char in pwd) >= 2):
           pw_strong = True


   return pwd
# pesan menyambut
print("selamat datang di password generator \nberikut adalah saran password dari kami untuk anda")
# variabel untuk perulangan
gajah = True
# perulangan selama variabel gajah tidak bernilai False
while gajah != False:
# untuk menginput masukkan user dan disimpan kedalam variabel beruang
    beruang = input("\ntekan enter untuk menampilkan password.\nketik selesai atau end untuk mengakhiri program -->")
# kondisi input user. jika user menginput selesai atau end. sebelum end atau selesai maka terjadi pengulangan
    if beruang == "selesai" or beruang == "end":
        gajah = False
        print("terimakasih anda telah menggunakan program kami.")
    else:
        print(f"berikut merupakan saran password kami \n \n {create_pw()}")
