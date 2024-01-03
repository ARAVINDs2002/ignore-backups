def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))

    edges.sort()
    parent = {vertex: vertex for vertex in graph}
    mst = []

    def find_set(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find_set(parent[vertex])
        return parent[vertex]

    def union(u, v):
        root_u = find_set(u)
        root_v = find_set(v)
        parent[root_u] = root_v

    for weight, u, v in edges:
        if find_set(u) != find_set(v):
            mst.append((u, v, weight))
            union(u, v)

    return mst


graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 1), ('D', 3)],
    'C': [('B', 1), ('D', 4)],
    'D': [('A', 5), ('B', 3), ('C', 4)]
}

minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
