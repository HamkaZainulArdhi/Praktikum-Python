# def heloworld():
#   print("helo world")
#   data = ["hamka", "ali"]
#   print(f"data adalah = {data}")

# heloworld()
# heloworld()
# heloworld()
# heloworld()
# heloworld()

# def fungsi_ambil_nama(nama):
#   print(nama + "ganteng")

# fungsi_ambil_nama("hamka")
# fungsi_ambil_nama("cieto")

# def perkalian(angka1, angka2):
#   hasil = angka1 * angka2
#   print(f"hasil nya adalah = \n{hasil}")

# perkalian(5, 5)

# def kali_dua(x):
#   return x * 2

# for i in range(5):
#   print(kali_dua(i))

def data_produk(nama, kategori):
  return f"produk: {nama}, Kategori: {kategori}"

for i in range(5):
  nama = input("masukan makanan : ")
  kategori = input("masukan kategori :")
  print(data_produk(nama, kategori))







