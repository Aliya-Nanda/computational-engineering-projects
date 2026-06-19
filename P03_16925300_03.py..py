#Nama/NIM:Nadiya Aliya Nanda
#Tanggal: 10/29/2025
#Deskripsi: Bingkisan Ulang Tahun 

"""
Nona Deb mau membungkus bingkisan ulang tahun. Setiap bingkisan diberi nomor dari x sampai y sebagai
penanda agar mudah untuk menyusunnya. Dua bingkisan akan dibungkus menjadi satu paket, satu angka
genap dan satu angka ganjil. Bingkisan tersebut akan dibungkus menjadi satu jika jumlah nomor keduanya
merupakan bilangan prima.

"""

#input
x = int(input("Nilai x: "))
y = int(input("Nilai y: "))

#proses
for i in range (x, y+1):
    if i % 2 != 0 :
        for j in range (x,y+1):
            if j % 2 == 0:
                jumlah = i + j 
                if jumlah > 1:
                    prima = True
                    for k in range(2, jumlah):
                        if jumlah % k == 0 : 
                            prima = False
                            break
#output
                    if prima:
                        print(i,j)

