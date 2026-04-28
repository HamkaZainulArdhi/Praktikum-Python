total_belanja = 150000

potongan_harga = 0

if total_belanja >= 200000:
  potongan_harga = 20000
elif total_belanja >= 100000:
  potongan_harga = 10000
else:
  potongan_harga = 0

total_bayar = total_belanja - potongan_harga

print("Total Belanja: Rp", total_belanja)

if potongan_harga > 0:
  print("Selamat anda mendapatkan potongan harga sebesar: Rp", potongan_harga)
else:
  print("Maaf, Anda tidak mendapatkan potongan harga")

print("Total yang harus dibayar: Rp", total_bayar)