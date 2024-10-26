Gaji=int(input("Gaji anda:"))
LamaBekerja=int(input("Berapa lama anda bekerja disini"))
if LamaBekerja>5:
    Bonus=Gaji*0.05
    print(f"Gaji:{Gaji}\nBonus: {Bonus} \nTotal:{Gaji+Bonus}")
else:
    print(f"Gaji:{Gaji}\n Mohon maaf anda belum memenuhi syarat mendapat bonus")