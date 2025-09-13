#Nama  : Muhammad Risky Alpianur
#NIM   : 2509116101
#Kelas : C
# Tema : Daftar Portofolio Trading

portofolio = []

print("=== Menu Portofolio Trading ===")
print("1. Tambahkan Aset")
print("2. Lihat Aset")

masukan = input("Pilih Menu (1-2): ")

if masukan == "1":
    nama = input("Masukan Nama Coin Crypto Atau Saham: ")
    jumlah = float(input("Masukan Jumlah Pembelian: "))
    beli = int(input("Masukan Harga Beli: "))
    portofolio =[nama, jumlah, beli] 

    print("\n=== Aset Berhasil Ditambahkan===")
    
else:
    print("Aset Tidak Terdaftar")

    print("\n=== Menu Portofolio Trading ===")
print("1. Tambahkan Aset")
print("2. Lihat Aset")
masukan = input("Pilih Menu (1-2): ")
if masukan == "2":
    print("\n==== Daftar Aset ====")
    print("Nama:", portofolio[0],"| Jumlah:", portofolio[1], "| Harga: Rp.", portofolio[2])

else:
    print("Input tidak valid")