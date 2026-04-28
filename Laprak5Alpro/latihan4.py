# Program untuk mencari nilai terbesar dari n angka
n = int(input("Masukkan jumlah data (n): "))

angka_list = []

for i in range(n):
    angka = int(input(f"Masukkan angka ke-{i + 1}: "))
    angka_list.append(angka)

nilai_terbesar = angka_list[0]

for angka in angka_list:
    if angka > nilai_terbesar:
        nilai_terbesar = angka

print(f"Nilai terbesar adalah: {nilai_terbesar}")
