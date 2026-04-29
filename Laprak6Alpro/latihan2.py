# buat fungsi untuk data produk dengan parms nama produk dan ketergori nya
# lalu di return
def data_produk(nama_product, kategori):
  return f"produk : {nama_product}, Ketegori : {kategori}"

# buat perulangan pake for
for i in range(5):
  print(f"\n data ke-{i+1}")
# buat variable untuk input
  nama = input("masukan nama produk : ")
  kategori = input("masukan kategori : ")

# buat variable untuk menampung hasil lalu print
  hasil = data_produk(nama, kategori)
  print(hasil)
