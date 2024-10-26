JumlahBarang=int(input("Berapa jumlah barang yang anda beli? "))
Harga= JumlahBarang*100

if Harga>1000 and Harga<2000:
    Diskon=Harga*0.1
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nHarga selruhnya:{Harga}\n Diskon:10%\n Total:{Harga - Diskon}")
elif Harga>2000 and Harga<3000:
    Diskon= Harga*0.2
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nHarga selruhnya:{Harga}\n Diskon:20%\n Total:{Harga-Diskon}")
elif Harga>3000 and Harga<4000:
    Diskon= Harga*0.3
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nHarga selruhnya:{Harga}\n Diskon:30%\n Total:{Harga-Diskon}")
elif Harga > 4000 and Harga < 5000:
    Diskon = Harga * 0.4
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nHarga selruhnya:{Harga}\n Diskon:40%\n Total:{Harga - Diskon}")
elif Harga>5000 and Harga<6000:
    Diskon= Harga*0.5
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nHarga selruhnya:{Harga}\n Diskon:50%\n Total:{Harga-Diskon}")
elif Harga>6000 and Harga<7000:
    Diskon= Harga*0.6
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nHarga selruhnya:{Harga}\n Diskon:60%\n Total:{Harga-Diskon}")
elif Harga>7000 and Harga<8000:
    Diskon= Harga*0.7
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nHarga selruhnya:{Harga}\n Diskon:70%\n Total:{Harga-Diskon}")
elif Harga>8000 and Harga<9000:
    Diskon= Harga*0.8
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nHarga selruhnya:{Harga}\n Diskon:80%\n Total:{Harga-Diskon}")
elif Harga>9000 and Harga<10000:
    Diskon= Harga*0.9
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nHarga selruhnya:{Harga}\n Diskon:90%\n Total:{Harga-Diskon}")
elif Harga>10000:
    Diskon= Harga*1
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nHarga selruhnya:{Harga}\n Diskon:100%\n Total:{Harga-Diskon}")
else:
    print(f"Jumlah barang: {JumlahBarang}\nHarga per barang: 100\nTotal:{Harga}")