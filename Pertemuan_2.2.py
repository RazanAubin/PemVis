# Buatlah program dengan menggunakan simple dialog dan messagebox

# Membuat program menghitung persegi panjang: luas dan keliling
# Membuat program menghitung segitiga: luas dan keliling
# Membuat program menghitung lingkaran: luas dan keliling
# Membuat program menghitung volume kubus
# Modifikasi program soal no.1, tampilkan persegi panjang dalam bentuk grafik


import tkinter as tk
from tkinter import simpledialog, messagebox

def hitung_segitiga(alas, tinggi, sisi1, sisi2):
    luas = 0.5 * int(alas) * int(tinggi)
    keliling = int(sisi1) + int(sisi2) + int(alas)
    return luas, keliling

ROOT = tk.Tk()
ROOT.withdraw()

# Meminta input panjang dan lebar dari pengguna menggunakan simpledialog
alas = simpledialog.askstring("Input", "Masukkan alas segitiga:")
tinggi = simpledialog.askstring("Input", "Masukkan tinggi segitiga:")
sisi1 = simpledialog.askstring("Input", "Masukkan sisi1 segitiga:")
sisi2 = simpledialog.askstring("Input", "Masukkan sisi2 segitiga:")

luas, keliling = hitung_segitiga(alas, tinggi, sisi1, sisi2)
ket = "Luas segitiga {0} dan {1} adalah {2}\nKeliling segitiga {0} dan {3} dan {4} adalah {5}".format(alas, tinggi, luas, sisi1, sisi2, keliling)

messagebox.showinfo("Message", ket)
