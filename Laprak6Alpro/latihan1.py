# fungsi luas persegi panjang 
def luas_persegi_panjang(panjang, lebar):
  return panjang * lebar

# fungsi luas segitiga
def luas_segitiga(alas, tinggi):
  return 0.5 * alas * tinggi

# input panjang dan lebar persegi panjang
panjang = float(input("masukan panjang persegi panjang :"))
lebar = float(input("masukan lebar persegi panjang :"))

# input panjang dan lebar segitiga
alas = float(input("masukan luas segitiga :"))
tinggi = float(input("masukan tinggi segitiga :"))

# buat variable untuk menampung hasil perhitungan
hasil_persegi = luas_persegi_panjang(panjang, lebar)
hasil_segitiga = luas_segitiga(alas, tinggi)

# tampilkan ke pada user / tampilkan pake print
print("----hasil----")
print(f"luas persegi panjang : {hasil_persegi} ")
print(f"luas segitiga : {hasil_segitiga} ")