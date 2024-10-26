import tkinter as t
import random as rd

w=t.Tk()
w.title=("Story generator")
w.geometry("1500x500")


 #functions
def story():


    global lb1
    global lb2
    global lb3
    global lb4
    kapan = ['Beberapa tahun lalu',
                'Kemarin', 'Minggu lalu',
                'Pada zaman dulu', 'Konon setiap tanggal 20 April']
    ber =   ["Ada 3 orang bersaudara","Ada 3 sekawan",
                 "Ada 3 orang yang bermusuhan","Ada 3 penguasa"]
    siapa = rd.choice(['seorang peri',
            'Anak kecil bernama Edward',
            'Penjelajah', 'Kucing',
            'Pangeran Shani'])
    siapa2 = rd.choice(['Atlet Anggar', 'Gadis kecil bernama  Mary',
                'Anjing', "Detektif Holmes",
              "Raja Alexander"])
    siapa3=rd.choice(["Ratu Elmira","Seorang Ilmuwan","Putri Desmawarni",
            "Benzi si ninja","seorang pejuang"])
    orang=[siapa,siapa3,siapa2]
    kota = ['Helsinki,Finlandia', 'Merauke,Indonesia', 'Maputo,Mozambik',
            'Bogota,Kolombia', 'Ngerulmud,Palau', "Managua,Nicaragua",
            "Guangzhong, Cina", "Hveragerði,Islandia","Boke,Guinea",
            "Rio Grande,Argentina","Nadi,Fiji","Iditarot,Amerika Serikat"]
    Lokasi = ["supermarket", 'pantai',
               'sekolah', 'istana', 'hutan',
              "museum","mall","karnaval"]
    kejadian1 = ['mendapat banyak teman karena kebaikannya', 'memenangkan lomba matematika',
                'memecahkan sebuah gelas dan terluka']
    kejadian2=["Menjadi sahabat sejati","Memecahkan puzzle bersama","Bermain petak umpet bersama","Berhasil membuat sebuah program, yaitu StoGen"]
    kj=rd.choice([kejadian1,kejadian2])
    p=rd.choice(kj)

    lb1.config(text=f"{rd.choice(kapan)}...")
    lb2.config(text=f"{rd.choice(ber)} yaitu {siapa},{siapa2},dan {siapa3}")
    lb3.config(text=f"Yang tinggal di kota {rd.choice(kota)}. Mereka pergi ke {rd.choice(Lokasi)}")
    if kj==kejadian1:
        t4=f"Disana {rd.choice(orang)} {p}"
        lb4.config(text=t4)
    if kj==kejadian2:
        t4=f"Disana mereka {p}"
        lb4.config(text=t4)


#widgets\
bt1=t.Button(w,text="Generate",command= story,font=("Arial",20))
lb1=t.Label(w,text="",font=("Arial Bold",25))
lb2=t.Label(w,text="",font=("Arial Bold",25))
lb3=t.Label(w,text="",font=("Arial Bold",25))
lb4=t.Label(w,text="",font=("Arial Bold",25))

#PLacement------>Peletakan Label,Dan button
bt1.pack()
lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()

w.mainloop()#---->Menampilkan Window