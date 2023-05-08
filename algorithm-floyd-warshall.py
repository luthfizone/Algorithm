# Mendefinisikan konstanta tak terhingga = INF
INF = float('inf')

# Matriks bobot dari grafik yang akan dihitung
data_asfia = [
    [0, 2.6, 12.3, 14.6, 14, INF, INF, INF],
    [2.6, 0, INF, 12.2, INF, 17.4, INF, INF],
    [12.3, INF, 0, INF, 9.9, INF, INF, 14.7],
    [14.6, 12.2, INF, 0, 18.9, 19.7, 13.9, INF],
    [14, INF, 9.9, 18.9, 0, INF, INF, 11.1],
    [INF, 17.4, INF, 19.7, INF, 0, 25.2, INF],
    [INF, INF, 14.7, INF, 11.1, INF, 27.5, 0]
]

# Jumlah simpul pada grafik
n = len(data_asfia)

# Fungsi untuk menghitung jarak terpendek menggunakan algoritma Floyd-Warshall


def floyd_warshall(data_asfia):
   # Membuat salinan matriks bobot pada variabel distance
    distance = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(data_asfia[i][j])
        distance.append(row)

    # Melakukan iterasi sebanyak n kali untuk mencari jarak terpendek
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Mencari jarak terpendek untuk setiap pasangan
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])

    # Mencetak hasil akhir
    print_solution(distance)

# Fungsi untuk mencetak hasil akhir


def print_solution(distance):
    for i in range(n):
        for j in range(n):
            # Jika jarak antara dua simpul tak terbatas, maka cetak INF
            if (distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="\t")
        print(" ")


# Memanggil fungsi floyd_warshall untuk menghitung jarak terpendek pada matriks bobot data_asfia
floyd_warshall(data_asfia)
