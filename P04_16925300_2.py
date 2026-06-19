#Nama/NIM:Nadiya Aliya Nanda/16925300
#Tanggal: 11/12/2025
#Deskripsi: PROGRAM BILANGAN FIBONACI LIMITED  

''' Bilangan Fibonacci adalah bilangan yang sangat terkenal dalam Matematika. Deret Fibonacci dimulai dari 0,
1, 1, 2, 3, 5, 8, dan seterusnya. Suatu bilangan Fibonacci adalah hasil dari penjumlahan dua bilangan Fibonacci
sebelumnya.
Tuan Vin melihat peluang yang besar dalam memanfaatkan bilangan Fibonacci ini. Ia ingin mendefinisikan
suatu jenis bilangan baru, yaitu bilangan limited-fibonacci. Bilangan limited-fibonacci adalah bilangan Fibonacci

yang tidak dapat dinyatakan sebagai jumlah dari dua bilangan kuadrat. Misalnya, 21 merupakan bilan-
gan limited-fibonacci, tetapi 13 bukan merupakan bilangan limited-fibonacci karena dapat dinyatakan sebagai

penjumlahan dua bilangan kuadrat, yaitu 22 + 3
2 = 13.

Pada suatu rentang bilangan bulat positif [L, R] inklusif, Tuan Vin ingin menentukan apa saja dan berapa
banyak bilangan limited-fibonacci.
Bantulah Tuan Vin membuat program yang bisa memenuhi kebutuhannya itu!

Catatan: Implementasikan fungsi/prosedur untuk menentukan apakah suatu bilangan merupakan penjumla-
han dua bilangan kuadrat. Diperbolehkan membuat fungsi/prosedur tambahan lainnya.'''

# Fungsi input
def input_data(): #INI FUNGSI 
    return int(input("Masukkan L: ")), int(input("Masukkan R: "))

def fibonacci(L, R): #INI FUNGSI 
    f = [1, 1]
    while f[-1] <= R:
        f.append(f[-1]+f[-2])
    return [x for x in f if L <= x <= R]

def limited_fib(fib_range): #INI PROSEDUR
    limited = []
    for n in fib_range:
        bisa = any(i*i + j*j == n for i in range(int(n**0.5)+1) for j in range(int(n**0.5)+1))
        if not bisa:
            limited.append(n)
    print("Banyak bilangan limited - fibonacci ::", len(limited))
    print("Bilangan  limited - fibonacci ::", *limited)

# Program utama dan outPUT
L, R = input_data()
fib_range = fibonacci(L,R)
limited_fib(fib_range)
