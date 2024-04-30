def bellman_ford(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

    # Check for negative cycles
    for u in graph:
        for v, w in graph[u].items():
            if distances[u] + w < distances[v]:
                print("Graph contains negative cycle")
                return

    return distances

# Example graph from the book
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {'B': 3, 'C': 1}
}

start_vertex = 'A'
distances = bellman_ford(graph, start_vertex)
print("Shortest distances from vertex", start_vertex, ": ", distances)
