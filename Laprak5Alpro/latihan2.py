# Program untuk menghitung penjumlahan bilangan 1 sampai n
n = int(input("Masukkan nilai n: "))

jumlah = 0

for i in range(1, n + 1):
    jumlah = jumlah + i

print(f"Jumlah bilangan dari 1 sampai {n} adalah: {jumlah}")
