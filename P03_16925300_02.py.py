#Nama/NIM:Nadiya Aliya Nanda
#Tanggal: 10/29/2025
#Deskripsi: Menetukan Mendapat Sushi Salmon dalam Conveyor Belt Sushi 

"""Nona Sal dan Nona Deb sedang berada di sebuah restoran sushi dengan sistem conveyor belt yang berbentuk
kotak berukuran N × N dengan N minimal bernilai 3. Karena restoran yang sangat ramai, Nona Sal dan Nona
Deb mendapat tempat duduk yang saling berhadapan, misal Nona Sal duduk di bagian utara conveyor belt
dan Nona Deb duduk di bagian selatan conveyor belt. Nona Sal yang sangat menyukai salmon belly nigiri ingin
mengetahui apakah dalam kurun suatu waktu bisa mendapatkan sushi tersebut dari conveyor belt. Nona Sal
juga telah meminta tolong Nona Deb untuk mengambilkan sushi tersebut jika berada di depannya. Bantulah
Nona Sal dan Nona Deb untuk menentukan apakah mereka bisa mendapatkan sushi salmon belly nigiri dari
conveyor belt tersebut!

"""

#input
n = int(input("Masukkan ukuran conveyor belt:"))

max_time = int(input("Masukkan waktu maksimal menunggu (detik):"))
sal_pos = (input("Masukkan posisi duduk Nona Sal:")).lower()

sushi_pos = int(input("Masukkan posisi sushi saat ini:"))

#proses
if sal_pos == "utara":
    sal_front = 1
    sushi_line = sushi_pos
elif sal_pos == "selatan":
    sal_front = n-2
    sushi_line = sushi_pos
elif sal_pos == "barat":
    sal_front = 1
    sushi_line = sushi_pos
else :
    sal_front = n-2
    sushi_line = sushi_pos

min_step = None
if sal_pos in ["utara","selatan"]:
    min_step = sushi_pos - (n//2)
else:
    min_step = sushi_pos - (n//2)

#output
if min_step <= max_time:
    print("Nona Sal berhasil mendapatkan sushi dalam waktu yang ditentukan .")
else:
    print("Nona Sal gagal mendapatkan sushi dalam waktu yang ditentukan .")