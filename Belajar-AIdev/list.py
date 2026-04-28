# # List

# # List adalah tipe data yang digunakan untuk menyimpan beberapa item dalam 
# # satu variabel. List dapat menyimpan berbagai jenis data, seperti angka, string, 
# # atau bahkan list lainnya. List juga bersifat mutable, 
# # artinya kita dapat mengubah isi list setelah dibuat. 


# data_angka = [1,2,3,4,5]
# print(data_angka)
# data_string = ["hamka", "tesa", "ali"]
# print(data_string)
# data_boolan = [True, False, True]
# print(data_boolan)
# data_campuran = ["hamka", 1, True, 2, "ali"]
# print(data_campuran)

# print("\ncara alternatif membuat list")
# data_range = range(0, 10) #range(start, stop, step)
# print(data_range)
# data_list = list(data_range)
# print(data_list)

# print("\ncara alternatif membuat list pake for")
# list_pake_for = [i**3 for i in range(0, 10)]
# print(list_pake_for)

# print("\ncara alternatif membuat list pake for if")
# list_pake_forif = [i for i in range(1, 10) if i != 5]
# print(list_pake_forif)


# list_pake_forif = [i for i in range(0, 10) if i > 1 ]
# print(list_pake_forif)

print("\nmanipulasi list")
data = ["hamka", "avril", "Habib"]
data1 = data[0]
print(data1)

data2 = data[-1]
print(data2)

data_len = len(data)
print(f"panjang data = {data_len}")

print(f"data sebelum di tambahkan = {data}")

# nama_baru = input("masukan nama baru =")

# data.insert(1, nama_baru) #insert(posisi, item)
# print(f"data setelah di tambahkan = {data}")

#menambahkan data di akhir
data.append("jajang") #append otomatis nambah di akhir
print(f"data setelah di tambahkan = {data}")

# menambahkan bnyk data baru
data_baru = ["aq", "bapa"]
data.extend(data_baru)
print(f"data baru = {data}")


#edit data list
data[2] = "azriel"
print(f"data baru {data}")

#data hapus
data.remove("azriel")
print(f"data baru {data}")

# hapus data paling akhir
data.pop()
print(f"data baru {data}")




