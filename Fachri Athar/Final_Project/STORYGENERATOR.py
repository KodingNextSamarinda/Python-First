import tkinter as t
import tkinter.messagebox as m
import tkinter.ttk as k
import random as rd

w=t.Tk()
w.title=("Story generator")
w.geometry("1975x1325")



#functions
def story():
    color=["BlueViolet","Aquamarine","DeepPink","DarkSalmon"]
    c=rd.choice(color)
    w.config(background=c)
    global lb1
    global lb2
    global lb3
    global lb4
    kapan = ['Beberapa tahun lalu',
                'Kemarin', 'Minggu lalu',
                'Pada zaman dulu', 'Konon setiap tanggal 20 April']
    ber =   ["Ada 3 orang bersaudara","Ada 3 sekawan",
                 "Ada 3 orang yang bermusuhan","Ada 3 penguasa"]
    siapa = ['seorang peri',
            'seorang anak kecil bernama Edward',
            'seorang penjelajah', 'seekor kucing',
            'Pangeran Shani']
    siapa2 = ['Seorang atlet', 'Gadis kecil bernama  Mary',
                'Seekor anjing', "Seorang detektif",
              "Raja Alexander"]
    siapa3=["Ratu Elmira","Seorang Ilmuwan","Putri Desmawarni",
            "Benzi si ninja","seorang pejuang"]
    orang1=rd.choice(siapa)
    orang2=rd.choice(siapa2)
    orang3=rd.choice(siapa3)
    pelaku=rd.choice([orang3,orang2,orang1])

    kota = ['Helsinki,Finlandia', 'Merauke,Indonesia', 'Maputo,Mozambik',
            'Bogota,Kolombia', 'Ngerulmud,Palau', "Managua,Nicaragua",
            "Guangzhong, Cina", "Hveragerði,Islandia","Boke,Guinea",
            "Rio Grande,Argentina","Nadi,Fiji","Iditarot,Amerika Serikat"]
    Lokasi = ["supermarket", 'pantai',
               'sekolah', 'istana', 'hutan',
              "museum","mall","karnaval"]
    kejadian1 = ['mendapat banyak teman karena kebaikannya', 'memenangkan lomba matematika',
                'memecahkan sebuah kasus',"Dimusuhi karena keanehannya",
                'bertahan dari ledakan bom, tapi yang lain tewas']
    kejadian2=["Menjadi sahabat sejati","Memecahkan puzzle bersama","Bermain petak umpet bersama",
               "Berperang satu sama lain"]
    kj=rd.choice([kejadian1,kejadian2])
    p=rd.choice(kj)

    lb1.config(text=f"{rd.choice(kapan)}...",background=c)
    lb2.config(text=f"{rd.choice(ber)} yaitu {orang1},{orang2},dan {orang3}",background=c)
    lb3.config(text=f"Yang tinggal di kota {rd.choice(kota)}. Mereka pergi ke {rd.choice(Lokasi)}",background=c)
    if kj==kejadian1:
        lb4.config(text=f"Disana,{pelaku},{p}",background=c)
    elif kj==kejadian2:
        lb4.config(text=f"Disana, mereka bertiga {p}",background=c)
    bt1.config(background=c)



#widgets\
cbbx
bt1=t.Button(w,text="Generate",command= story,font=("Arial Bold",18))
lb1=t.Label(w,text="",font=("Arial Bold",25))
lb2=t.Label(w,text="",font=("Arial Bold",25))
lb3=t.Label(w,text="",font=("Arial Bold",25))
lb4=t.Label(w,text="",font=("Arial Bold",25))



bt1.pack()
lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()



w.mainloop()