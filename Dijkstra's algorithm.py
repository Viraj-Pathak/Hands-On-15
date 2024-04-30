import heapq

def dijkstra(graph, start):
    # Initialize distances to all vertices as infinity
    distances = {vertex: float('inf') for vertex in graph}
    # Distance from start vertex to itself is 0
    distances[start] = 0
    
    # Priority queue to store vertices with their distances
    pq = [(0, start)]
    
    while pq:
        # Pop vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(pq)
        
        # If current distance is greater than already computed distance, skip
        if current_distance > distances[current_vertex]:
            continue
        
        # Explore neighbors of current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Update distance if shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add neighbor to priority queue
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example graph from the book
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex, ":", distances)
