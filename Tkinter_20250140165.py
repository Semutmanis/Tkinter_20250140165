import tkinter as tk
import tkinter.messagebox as msg

top = tk.Tk()
labelframe = tk.LabelFrame(top, text= "-- Aplikasi Prediksi Prodi Pilihan --")
labelframe.pack(expand= "yes", anchor= "center")
l1 = tk.Label(labelframe, text= "Teknologi Server");l1.pack()
e1 = tk.Entry(labelframe, bd = 5);e1.pack()