# copy list
a = ["hamka", "zain", "tesa"]
print(f"data a , {a}")

b = a # by reference
print(f"data a , {b}")

# semisal aku mau ubah salah satu data di b
b[0] = "olahh"
print(f"data a , {b}")
print(f"data a , {a}")

print(f"addres = {hex(id(a))}")
print(f"addres = {hex(id(b))}")

c = a.copy()
print(f"data c = {c}")

# ubah data c
c[1] = "toy"
print(f"data c = {c}")

print(f"data a , {b}")
print(f"data a , {a}")

print(f"addres = {hex(id(c))}")

# data di variable rujukan jika di ubah akan mengubah varible turunan nya
# tapi jika yg di ubah di varibel turunannnya , maka data varibale rujukan tidak terubah