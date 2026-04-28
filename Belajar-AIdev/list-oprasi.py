# count data
data = [1,2,3,2,5,3,4,5,4,5,4.5,3,4,5]

data5 = data.count(5)
print(f"data angka lima ada = {data5}")

data3 = data.count(4)
print(f"data 3 ada = {data3}")

# Posisi data
data_nama = ["hamka", "avril", "zee"]
datahamka = data_nama.index("avril")

print(f"data hamka ada di {datahamka}")

# bagaiamana mengurutkan list
data.sort()
print(f"data setelah di sort \n {data}")


data_nama.sort()
print(f"data nama sort \n {data_nama}")

data.reverse()
print(f"data nama di balikin \n {data}")