# Buatlah program dengan menggunakan simple dialog dan messagebox

# Membuat program menghitung persegi panjang: luas dan keliling
# Membuat program menghitung segitiga: luas dan keliling
# Membuat program menghitung lingkaran: luas dan keliling
# Membuat program menghitung volume kubus
# Modifikasi program soal no.1, tampilkan persegi panjang dalam bentuk grafik


import tkinter as tk
from tkinter import simpledialog, messagebox

def hitung_lingkaran(phi, r):
    luas = phi * int(r) ** 2
    keliling = 2 * phi * int(r)
    return luas, keliling

ROOT = tk.Tk()
ROOT.withdraw()

# Meminta input panjang dan lebar dari pengguna menggunakan simpledialog
r = simpledialog.askstring("Input", "Masukkan jari - jari lingkaran:")
phi = 3.14

luas, keliling = hitung_lingkaran(phi, r)
ket = "Luas lingkaran dengan jari-jari {0} dan adalah {1}\nKeliling lingkaran dengan jari-jari {0} adalah {2}".format(r, luas, keliling)

messagebox.showinfo("Message", ket)
