# Buatlah program dengan menggunakan simple dialog dan messagebox

# Membuat program menghitung persegi panjang: luas dan keliling
# Membuat program menghitung segitiga: luas dan keliling
# Membuat program menghitung lingkaran: luas dan keliling
# Membuat program menghitung volume kubus
# Modifikasi program soal no.1, tampilkan persegi panjang dalam bentuk grafik


import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt

def hitung_persegi_panjang(panjang, lebar):
    luas = int(panjang) * int(lebar)
    keliling = 2 * (int(panjang) + int(lebar))
    return luas, keliling

def gambar_persegi_panjang(panjang, lebar):
    plt.figure()
    plt.gca().add_patch(plt.Rectangle((0, 0), int(panjang), int(lebar), edgecolor='black', facecolor='lightblue'))
    plt.xlim(0, int(panjang) + 5)
    plt.ylim(0, int(lebar) + 5)
    plt.title('Gambar Persegi Panjang')
    plt.xlabel('Panjang')
    plt.ylabel('Lebar')
    plt.grid()
    plt.show()

ROOT = tk.Tk()
ROOT.withdraw()

# Meminta input panjang dan lebar dari pengguna menggunakan simpledialog
panjang = simpledialog.askstring("Input", "Masukkan panjang persegi panjang:")
lebar = simpledialog.askstring("Input", "Masukkan lebar persegi panjang:")

luas, keliling = hitung_persegi_panjang(panjang, lebar)
ket = "Luas persegi panjang {0} dan {1} adalah {2}\nKeliling persegi panjang adalah {3}".format(panjang, lebar, luas, keliling)

messagebox.showinfo("Message", ket)

# Menampilkan persegi panjang dalam bentuk grafik
gambar_persegi_panjang(panjang, lebar)
