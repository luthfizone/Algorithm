INF = float("inf")

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
    distance = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(data_asfia[i][j])
        distance.append(row)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

result = floyd_warshall(data_asfia)

# Cetak semua hasil perhitungan

print("Matriks jarak terpendek antar simpul:")
for i in range(n):
    for j in range(n):
        if result[i][j] == INF:
            print("INF", end="\t")
        else:
            print("{:.1f}".format(result[i][j]), end="\t")
    print()

print()

print("Jarak terpendek dari setiap simpul ke simpul lain:")
for i in range(n):
    for j in range(n):
        if i != j:
            print("Simpul", i, "ke simpul", j, ":", "{:.1f}".format(result[i][j]))


def get_shortest_distance(origin, destination):
    return result[origin][destination]

print("\n")
# Contoh penggunaan fungsi get_shortest_distance dengan input dari terminal
origin = int(input("Masukkan simpul asal: "))
destination = int(input("Masukkan simpul tujuan: "))

jarak_terpendek = get_shortest_distance(origin, destination)
print(f"Jarak terpendek dari simpul {origin} ke simpul {destination}: {jarak_terpendek}")

# Menggunakan hasil perhitungan dalam pengolahan data baru
jarak_03 = get_shortest_distance(0, 3)
jarak_25 = get_shortest_distance(2, 5)

# Melakukan operasi atau pemrosesan data dengan menggunakan jarak terpendek
total_jarak = jarak_03 + jarak_25
print("Total jarak dari simpul 0 ke simpul 3 dan simpul 2 ke simpul 5:", total_jarak)
