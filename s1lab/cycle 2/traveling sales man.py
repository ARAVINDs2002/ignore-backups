import numpy as np

def nearest_neighbor(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    tour = [start]
    visited[start] = True
    current_node = start
    for _ in range(num_nodes - 1):
        nearest_neighbor = min((node for node in range(num_nodes) if not visited[node]), 
                               key=lambda x: graph[current_node][x])
        tour.append(nearest_neighbor)
        visited[nearest_neighbor] = True
        current_node = nearest_neighbor
    tour.append(start)  # Complete the tour
    return tour

def total_distance(graph, tour):
    total = 0
    for i in range(len(tour) - 1):
        total += graph[tour[i]][tour[i+1]]
    return total

def tsp(graph):
    num_nodes = len(graph)
    start_node = 0
    initial_tour = nearest_neighbor(graph, start_node)
    best_tour = initial_tour
    min_distance = total_distance(graph, initial_tour)
    stack = [(start_node, initial_tour, min_distance)]
    
    while stack:
        current_node, current_tour, current_distance = stack.pop()
        for next_node in range(num_nodes):
            if next_node not in current_tour:
                new_tour = current_tour[:]
                new_tour.insert(-1, next_node)  # Insert before the last element (the starting node)
                new_tour_distance = current_distance + graph[current_node][next_node]
                if len(new_tour) == num_nodes + 1:
                    new_tour_distance += graph[next_node][start_node]  # Complete the tour
                    if new_tour_distance < min_distance:
                        best_tour = new_tour
                        min_distance = new_tour_distance
                else:
                    if new_tour_distance < min_distance:
                        stack.append((next_node, new_tour, new_tour_distance))
    return best_tour, min_distance

# Example graph represented as an adjacency matrix
graph = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])

# Solve TSP using branch and bound with greedy initial tour
best_tour, min_distance = tsp(graph)
print("Best Tour:", best_tour)
print("Minimum Distance:", min_distance)
