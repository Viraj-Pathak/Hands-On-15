def floyd_warshall(graph):
    num_vertices = len(graph)
    distances = [[float('infinity')] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        distances[i][i] = 0

    for vertex1 in graph:
        for vertex2, weight in graph[vertex1].items():
            distances[vertex1][vertex2] = weight

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

# Example graph from the book
graph = {
    0: {1: 3, 2: 8, 4: -4},
    1: {3: 1, 4: 7},
    2: {1: 4},
    3: {0: 2, 2: -5},
    4: {3: 6}
}

all_distances = floyd_warshall(graph)
print("All-pairs shortest distances:")
for i in range(len(all_distances)):
    print(all_distances[i])
