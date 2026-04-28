# Program untuk menampilkan pola segitiga angka
n = int(input("Masukkan ukuran pola (n): "))

print("Pola Segitiga Angka:")

for i in range(1, n + 1):
    # spasi di depan
    for j in range(n - i):
        print(" ", end=" ")
    
    # bintang
    for k in range(2 * i - 1):
        print("*", end=" ")
    
    print()