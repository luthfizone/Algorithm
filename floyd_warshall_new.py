INF = float("inf")

# Matriks jarak antar simpul
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

n = len(data_asfia)

def floyd_warshall(data_asfia):
    # Matriks jarak terpendek awal
    distance = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(data_asfia[i][j])
        distance.append(row)

    # Algoritma Floyd-Warshall untuk mencari jarak terpendek
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

result = floyd_warshall(data_asfia)

def get_shortest_distance(origin, destination):
    # Mendapatkan jarak terpendek dari simpul asal ke simpul tujuan
    return result[origin][destination]

# Fungsi untuk menghitung total jarak antara dua pasang simpul
def calculate_total_distance(origin1, destination1, origin2, destination2):
    jarak1 = get_shortest_distance(origin1, destination1)
    jarak2 = get_shortest_distance(origin2, destination2)
    return jarak1 + jarak2

# Cetak semua hasil perhitungan matriks jarak terpendek antar simpul
print("Matriks jarak terpendek antar simpul:")
for i in range(n):
    for j in range(n):
        if result[i][j] == INF:
            print("INF", end="\t")
        else:
            print("{:.1f}".format(result[i][j]), end="\t")
    print()

print()

# Cetak jarak terpendek dari setiap simpul ke simpul lain
print("Jarak terpendek dari setiap simpul ke simpul lain:")
for i in range(n):
    for j in range(n):
        if i != j:
            print("Simpul", i, "ke simpul", j, ":", "{:.1f}".format(result[i][j]))

# Meminta input dari pengguna untuk pengolahan data baru
origin1 = int(input("Masukkan simpul asal pertama: "))
destination1 = int(input("Masukkan simpul tujuan pertama: "))
origin2 = int(input("Masukkan simpul asal kedua: "))
destination2 = int(input("Masukkan simpul tujuan kedua: "))

# Menghitung total jarak dari dua pasang simpul yang dimasukkan pengguna
total_jarak = calculate_total_distance(origin1, destination1, origin2, destination2)

# Cetak total jarak dari dua pasang simpul
print("Total jarak dari simpul", origin1, "ke simpul", destination1, "dan simpul", origin2, "ke simpul", destination2, ":", total_jarak)
