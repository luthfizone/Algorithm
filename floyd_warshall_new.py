# Mendefinisikan konstanta tak hingga dengan INF
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
def floyd_warshall(data_asfia):
    # Membuat salinan matriks data_asfia pada variabel distance
    distance = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(data_asfia[i][j])
        distance.append(row)

    # Inisialisasi matriks jalur untuk menyimpan jalur terpendek antar simpul
    path = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and distance[i][j] != INF:
                path[i][j] = i

    # Algoritma Floyd-Warshall untuk mencari jarak terpendek dan jalur terpendek
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    path[i][j] = path[k][j]

    print_solution(distance, path)

# Fungsi untuk mencetak hasil akhir termasuk jalur terpendek
def print_solution(distance, path):
    print("Matriks jarak terpendek antar simpul:")
    for i in range(n):
        for j in range(n):
            if distance[i][j] == INF:
                print("INF", end="\t")
            else:
                print("{:.1f}".format(distance[i][j]), end="\t")
        print()

    print("\nJarak terpendek dari setiap simpul ke simpul lain:\n")
    for i in range(n):
        for j in range(n):
            if i != j:
                print("Simpul", i, "ke simpul", j, ":", "{:.1f}".format(distance[i][j]))

    print("\nJalur terpendek antar simpul:\n")
    for i in range(n):
        for j in range(n):
            if i != j:
                print("Simpul", i, "ke simpul", j, ": ", end="")
                print_path(i, j, path)
                print(j)
    print()

# Fungsi rekursif untuk mencetak jalur terpendek antar simpul
def print_path(start, end, path):
    if start == end:
        print(start, end=" -> ")
    elif path[start][end] is None:
        print("Tidak ada jalur dari", start, "ke", end)
    else:
        print_path(start, path[start][end], path)
        print(path[start][end], end=" -> ")

# Memanggil fungsi floyd_warshall untuk menghitung jarak terpendek dan jalur terpendek pada matriks data_asfia
floyd_warshall(data_asfia)
