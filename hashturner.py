__author__ = "omeregri"

import tkinter as tk
import hashlib


root = tk.Tk()
root.title('HashTurner')
root.geometry('500x150')
root.maxsize(500,150)
root.minsize(500,150)

def hashturner():
    kelime = kelime_girisi.get()
    kelime_girisi.delete(0, 'end')
    hashlib_kelime = hashlib.md5(kelime.encode()).hexdigest()
    global x
    x = hashlib_kelime
    kelime_girisi.insert(0, x)

def copy_hash():
    root.clipboard_append(x)
baslik = tk.Label(root, text="HashTurner", font=('Helvetica',12,'bold'))
baslik.place(x=210,y=10)

yazi = tk.Label(root, text="İstediğiniz Kelimeyi Girin:", font=('verdana', 10, 'bold'))
yazi.place(x=8, y=65)
kelime_girisi = tk.Entry(root)
kelime_girisi.place(x=199, y=65)

donustur = tk.Button(root, text='Dönüştür', command=hashturner)
donustur.place(x=340, y=65)

kopyala = tk.Button(root, text="Kopyala", command=copy_hash)
kopyala.place(x=400, y=65)
root.mainloop()
