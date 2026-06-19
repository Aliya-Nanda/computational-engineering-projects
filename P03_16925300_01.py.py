#Nama/NIM:Nadiya Aliya Nanda
#Tanggal: 10/29/2025
#Deskripsi: Deret Fibonnaci

""" Nona Sal sedang belajar tentang deret Fibonacci dan penasaran apakah sebuah array angka yang diberikan
membentuk sebagian dari deret Fibonacci atau tidak. Deret Fibonacci adalah deret dimana setiap angka adalah
hasil penjumlahan dua angka sebelumnya (contoh: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...). Nona Sal ingin mengecek apakah
dari sebuah deret terdapat subsequence yang membentuk deret Fibonacci murni. Bantulah Nona Sal untuk
membuat program yang dapat menentukan apakah deret yang diberikan merupakan deret Fibonacci murni
atau tidak dan jika tidak, program harus mengidentifikasi subsequence terpanjang yang membentuk deret
Fibonacci.

"""
#input
n = int(input("Masukkan jumlah elemen: "))

#proses
deret = []
for i in range(n):
    angka = int(input(f"elemen ke-{i+1}:"))
    deret.append(angka)

murni = True
for i in range (2,n):
    if deret[i] != deret [i-1] + deret [1-2]:
        murni = False
        break
#output
if murni:
    print("Deret tersebut merupakan deret Fibonacci murni.")
else:
    panjang = 2
    max_panjang = 2
    start_index = 0
    for i in range (2,n):
        if deret[i] == deret[i-1] + deret[i-2]:
            panjang += 1
            if panjang > max_panjang:
                max_panjang = panjang
        else: 
            panjang = 2 
    end_index = start_index + max_panjang - 1
    print ("Deret tersebut bukan merupakan deret Fibonacci .")
    print(f"Deret tersebut bukan deret Fibonacci murni dengan panjang subsequence Fibonacci terpanjang {max_panjang} elemen , dari indeks 0 sampai {max_panjang-1}")