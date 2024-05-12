def prim(graph):
    # Initialize an empty set to keep track of visited vertices
    visited = set()
    # Initialize a list to store the edges of the minimum spanning tree
    min_spanning_tree = []
    
    # Start from the first vertex (index 0)
    current_vertex = 0
    visited.add(current_vertex)
    
    # Continue until all vertices are visited
    while len(visited) < len(graph):
        # Find the minimum weight edge connecting a visited vertex to an unvisited vertex
        min_weight = float('inf')
        min_edge = None
        for src in visited:
            for dest, weight in enumerate(graph[src]):
                if dest not in visited and weight != 0 and weight < min_weight:
                    min_weight = weight
                    min_edge = (src, dest, weight)
        
        # Add the minimum weight edge to the minimum spanning tree
        min_spanning_tree.append(min_edge)
        
        # Mark the destination vertex of the minimum weight edge as visited
        visited.add(min_edge[1])
    
    return min_spanning_tree

# Example graph represented as an adjacency matrix
graph = [
    [0, 2, 0, 6, 0],  # Vertex 0
    [2, 0, 3, 8, 5],  # Vertex 1
    [0, 3, 0, 0, 7],  # Vertex 2
    [6, 8, 0, 0, 9],  # Vertex 3
    [0, 5, 7, 9, 0]   # Vertex 4
]

min_spanning_tree = prim(graph)
print("Minimum Spanning Tree Edges:")
for edge in min_spanning_tree:
    print("Edge:", edge)
