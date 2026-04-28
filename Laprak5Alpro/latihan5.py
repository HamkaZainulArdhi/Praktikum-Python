# Program untuk menampilkan persegi angka n x n
n = int(input("Masukkan ukuran persegi (n): "))

print(f"Persegi Angka {n} x {n}:")

for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()
