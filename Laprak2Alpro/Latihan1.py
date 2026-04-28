daftar_belanja = []

for i in range (5):
  barang = input(f"Masukkan barang ke-{i+1} :")
  daftar_belanja.append(barang)

print("\n==Daftar Barang==")
print(daftar_belanja)

print("Barang pertama :", daftar_belanja[0])
print("Barang Terakhir :", daftar_belanja[-1])

print("Jumlah Barang :", len(daftar_belanja))

print("\nIsi daftar belanja :")
for barang in daftar_belanja:
  print("-", barang)

hapus = input("\nMasukkan nama barang yang ingin dihapus:")
daftar_belanja.remove(hapus)

print("\nDaftar setelah dihapus :")
print(daftar_belanja)