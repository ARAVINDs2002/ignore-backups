import numpy as np
import queue

class Node:
    def __init__(self, path, bound):
        self.path = path
        self.bound = bound

    def __lt__(self, other):
        return self.bound < other.bound

    def __eq__(self, other):
        return self.bound == other.bound

def tsp_branch_and_bound(graph):
    n = graph.shape[0]
    vertices = set(range(n))

    # Priority queue to store nodes with their bounds
    pq = queue.PriorityQueue()

    # Initialize with the starting city (A) and an empty path
    initial_path = [0]
    initial_bound = get_bound(graph, initial_path)
    initial_node = Node(path=initial_path, bound=initial_bound)

    # Add the initial node to the priority queue
    pq.put(initial_node)

    # Initialize variables for the best solution
    min_distance = np.inf
    optimal_route = None

    while not pq.empty():
        # Get the node with the minimum bound
        current_node = pq.get()

        # Prune if the current bound is greater than the minimum distance
        if current_node.bound >= min_distance:
            continue

        last_city = current_node.path[-1]

        # Explore all cities
        for city in vertices - set(current_node.path):
            new_path = current_node.path + [city]
            new_bound = current_node.bound + graph[last_city, city] + get_bound(graph, new_path)

            if len(new_path) == n:
                # Reached the end of the path
                distance = new_bound + graph[city, 0]
                if distance < min_distance:
                    min_distance = distance
                    optimal_route = new_path
            else:
                # Add the new node to the priority queue
                pq.put(Node(path=new_path, bound=new_bound))

    return min_distance, optimal_route

def get_bound(graph, path):
    bound = 0
    last_city = path[-1]

    # Reduce rows
    bound += np.min(graph[last_city, :])

    # Reduce columns
    bound += np.min(graph[:, path], axis=0).sum()

    return bound

# Example usage:
vertices = ['A', 'B', 'C', 'D']
distances = np.array([
    [0, 2, 5, 8],
    [2, 0, 3, 1],
    [5, 3, 0, 1],
    [8, 1, 1, 0]
])

graph = distances.copy()

min_distance, optimal_route = tsp_branch_and_bound(graph)

# Print the result
print("Optimal Route:", [vertices[i] for i in optimal_route])
print("Minimum Distance:", min_distance)