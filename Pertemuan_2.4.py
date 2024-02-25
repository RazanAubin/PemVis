# Buatlah program dengan menggunakan simple dialog dan messagebox

# Membuat program menghitung persegi panjang: luas dan keliling
# Membuat program menghitung segitiga: luas dan keliling
# Membuat program menghitung lingkaran: luas dan keliling
# Membuat program menghitung volume kubus
# Modifikasi program soal no.1, tampilkan persegi panjang dalam bentuk grafik


import tkinter as tk
from tkinter import simpledialog, messagebox

def hitung_kubus(V):
    volume = int(V) ** 3
    return volume

ROOT = tk.Tk()
ROOT.withdraw()

# Meminta input panjang dan lebar dari pengguna menggunakan simpledialog
V = simpledialog.askstring("Input", "Masukkan sisi kubus:")

volume = hitung_kubus(V)
ket = "Volume kubus dengan rumus s x s x s, dengan sisi {0} dan adalah {1}".format(V, volume)

messagebox.showinfo("Message", ket)
