def kruskal(graph):
    num_vertices = len(graph)
    
    # Step 1: Sort all the edges by their weights
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2])

    # Step 2: Initialize an empty list to store the minimum spanning tree edges
    min_spanning_tree = []

    # Step 3: Iterate through sorted edges and add to minimum spanning tree if no cycle is formed
    parent = [i for i in range(num_vertices)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        parent[x_root] = y_root

    for edge in edges:
        src, dest, weight = edge
        if find(src) != find(dest):
            union(src, dest)
            min_spanning_tree.append(edge)

    return min_spanning_tree

# Example graph represented as an adjacency matrix
graph = [
    [0, 2, 0, 6, 0],  # Vertex 0
    [2, 0, 3, 8, 5],  # Vertex 1
    [0, 3, 0, 0, 7],  # Vertex 2
    [6, 8, 0, 0, 9],  # Vertex 3
    [0, 5, 7, 9, 0]   # Vertex 4
]

min_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree Edges:")
for edge in min_spanning_tree:
    print("Edge:", edge)
