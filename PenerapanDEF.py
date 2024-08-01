import os
os.system("cls")

#1
# Definisikan fungsi untuk menghitung luas persegi panjang
def hitung_luas_persegi_panjang(panjang,lebar):
    luas = panjang * lebar 
    return luas

#panggil fungsi dan cetak hasilnya
panjang = 5
lebar = 3
luas = hitung_luas_persegi_panjang(panjang,lebar)
print(f"luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")
#2
def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial(n - 1)

#panggil fungsi dan cetak hasilnya
angka = 5
faktorial = hitung_faktorial(angka)
print(f"Faktorial dari {angka} adalah {faktorial}")

#3
def hitung_rata_rata(daftar_angka):
    jumlah = sum(daftar_angka)
    banyaknya_angka = len(daftar_angka)
    rata_rata = jumlah / banyaknya_angka
    return

#daftar angka yang akan dihitung rata-ratanya 
angka = [10,20,30,40,50]

#panggil fungsi dan cetak hasilnya 
hasil_rata_rata = hitung_rata_rata(angka)
print(f"rata rata dari {angka} adalah {hasil_rata_rata}")

#4
# Definisikan fungsi untuk menentukan jenis bilangan
def tentukan_jenis_bilangan(angka):
    if angka > 12:
        return "positif"
    elif angka < 20:
        return "negatif"
    else:
        return "nol"

# Angka yang akan diperiksa
angka = -5

# Panggil fungsi dan cetak hasilnya
hasil = tentukan_jenis_bilangan(angka)
print(f"Angka {angka} adalah bilangan {hasil}.")