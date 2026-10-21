import tkinter as tk
import tkinter.messagebox as msg

top = tk.Tk()
labelframe = tk.LabelFrame(top, text= "-- Aplikasi Prediksi Prodi Pilihan --")
labelframe.pack(expand= "yes", anchor= "center")
l1 = tk.Label(labelframe, text= "Teknologi Server");l1.pack()
e1 = tk.Entry(labelframe, bd = 5);e1.pack()
l2 = tk.Label(labelframe, text= "Statiska");l2.pack()
e2 = tk.Entry(labelframe, bd = 5);e2.pack()
l3 = tk.Label(labelframe, text= "Implementasi Basis Data");l3.pack()
e3 = tk.Entry(labelframe, bd = 5);e3.pack()
l4 = tk.Label(labelframe, text= "Matematika");l4.pack()
e4 = tk.Entry(labelframe, bd = 5);e4.pack()