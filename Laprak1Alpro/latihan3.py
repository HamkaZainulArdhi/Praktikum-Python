# meminta user input
panjang = input("masukan panjang persegi panjang: ")  
lebar = input("masukan lebar persegi panjang: ")

# mengubah ke tipe data float
panjang = float(panjang)
lebar = float(lebar)

# menghitung luas dan keliling nya
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# menampilkan hasil nya
print('Hasil dari perhitungan tersebut adalah : ')
print('Luas adalah ', luas)
print('Keliling adalah ', keliling)