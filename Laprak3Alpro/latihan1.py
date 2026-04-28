gaji_pokok = float(input("Masukkan Gaji Pokok: "))
tunjangan_transport = float(input("Masukkan Tunjangan Transport: "))
jam_lembur = float(input("Masukkan Jumlah Jam Lembur: "))
tarif_lembur = float(input("Masukkan Tarif Lembur per Jam: "))

uang_lembur = jam_lembur * tarif_lembur
gaji_kotor = gaji_pokok + tunjangan_transport + uang_lembur
pajak = 0.05 * gaji_kotor
gaji_bersih = gaji_kotor - pajak

print("\n===Rincian Gaji===")
print("Gaji Kotor : ", gaji_kotor)
print("Potongan Pajak : ", pajak)
print("Gaji Bersih : ", gaji_bersih)