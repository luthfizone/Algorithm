# Mendefinisikan konstanta tak hingga dengan INF
"""
Jadi gampangnya INF itu buat pengganti data asfia yang
tak terhingga
"""
INF = float('inf')

# Matriks data punya asfia yang akan dihitung
data_asfia = [
    [0, 2.6, 12.3, 14.6, 14, INF, INF, INF],
    [2.6, 0, INF, 12.2, INF, 17.4, INF, INF],
    [12.3, INF, 0, INF, 9.9, INF, INF, 14.7],
    [14.6, 12.2, INF, 0, 18.9, 19.7, 13.9, INF],
    [14, INF, 9.9, 18.9, 0, INF, INF, 11.1],
    [INF, 17.4, INF, 19.7, INF, 0, 25.2, INF],
    [INF, INF, INF, 13.9, INF, 25.2, 0, 27.5],
    [INF, INF, 14.7, INF, 11.1, INF, 27.5, 0]
]

# Panjang jumlah data pada 
n = len(data_asfia) # datanya ada 7 karena dihitung index dari 0 - 8 bukan dari 1-8

# Fungsi untuk menghitung jarak terpendek menggunakan algoritma Floyd-Warshall

"""
Maksud dari kode dibawah gampangnya terdapat variabel distance yang 
di masukin data tabel diatas dengan range perulangannya itu 7
"""
def floyd_warshall(data_asfia):
   # Membuat salinan matriks data kamu pada variabel distance
    distance = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(data_asfia[i][j])
        distance.append(row)
        
 """
 PENTING...

Kode dibawah ini menjelaskan bagaimana caranya algoritma floyd-warshall bekerja
dimulai dari terdapatnya 3 perulangan (iterasi) yang digunakan untuk mengakses
setiap elemen dalam matriks data distance secara berulang-ulang.

Perulangan k digunakan buat ngecek setiap simpul seagai simpul perantara yang
mungkin dapat memperbarui jarak terpendek antara dua simpul yang lain.

Perulangan i digunakan buat mengiterasi (perulangan) simpul-simpul asal,

Perulangan j digunakan untuk melakukan iterasi perulangan simpul-simpul tujuan

Kemudian membuat variabel distance[i][j] dengan arti dari:
- distance[i][j] : mempresentasikan jarak terpendek antara simpul i dan j
- distance[i][k] : mempresentasikan jarak antara simpul i dan simpul perantara k
- distance[k][j] : mempresentasikan jarak antara simpul perantara k dan simpul j

Dalam setiap perulangan, jarak terpendek antara simpul i dan j akan diperbaharui jika
ditemukan jalur baru melalui simpul perantara k yang lebih pendek daripada jalur sebelumnya.

Proses ini dilakukan secara berulang-ulang hingga ditemukan jalur terpendek antara setiap
pasangan simpul dalam grafik data sumber

"""

    # Melakukan iterasi sebanyak n kali untuk mencari jarak terpendek
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Mencari jarak terpendek untuk setiap pasangan
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])


    # Mencetak hasil akhir dari simpul yang telah dibuat diatas
    print_solution(distance)

# Kemudian membuat fungsi untuk mencetak hasil akhir

"""
Kode dibawah berfungsi untuk mencetaknya di terminal..

Pada baris pertama terdapat perulangan menggunakan range(n)
yang digunakan untuk mengakses setiap elemen dalam matriks jarak
distance yang merupakan matriks dengan ukuran 'n' x 'n' dan berisi
jarak terpendek antara simpul-simpul pada grafik

Pada setiap iterasi, baris 'if' digunakan untuk mengecek apakah jarak
antara dua simpul yang sedang diperiksa tidak terbatas atau tak terhingga,
jika jarak antara dua simpul tak terbatas, maka akan dicetak string "INF"
dengan tambahan spasi untuk memisahkan setiap elemen, sedangkan jika jarak antara dua
simpul terdefinisi, maka nilai jarak tersebut akan dicetak dengan tambahan tab('\t')
sebagai pemisah antara setiap elemen

Pada akhir setiap iterasi (perulangan dalam perulangan 'j', diperintahkan untuk
'print(" ")' digunakan untuk mencetak baris baru sehingga output hasil cetakan matriks
jarak terpendek antar simpul menjadi lebih terstruktur dan mudah dibaca,

Kode tersebut dapat digunakan untuk mencetak solusi dari algoritma floyn-warshall dalam
format matriks dengan ukuran 'n' x 'n'
"""

def print_solution(distance):
    for i in range(n):
        for j in range(n):
            # Jika jarak antara dua simpul tak terbatas, maka cetak INF dan berikan string kosong
            if (distance[i][j] == INF):
                print("INF", end=" ")
            # Jika karak antara dua simpul tak terbatas, maka cetak hasilnya, dan berikan \t atau tab
            else:
                print("{:.1f}".format(distance[i][j]), end="\t")
            # print dibawah dibutuhkan untuk memisahkan per baris data yang akan digunakan, semisal tidak pakai ini maka akan di print 16 data menyamping
        print(" ")
        



# Memanggil fungsi floyd_warshall untuk menghitung jarak terpendek pada matriks bobot data_asfia
floyd_warshall(data_asfia)
