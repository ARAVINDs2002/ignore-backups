import heapq


def prim(graph):
    mst = []
    start_vertex = list(graph.keys())[0]
    heap = [(0, start_vertex, None)]
    visited = set()

    while heap:
        weight, current_vertex, prev_vertex = heapq.heappop(heap)

        if current_vertex not in visited:
            visited.add(current_vertex)

            if prev_vertex is not None:
                mst.append((prev_vertex, current_vertex, weight))

            for neighbor, neighbor_weight in graph[current_vertex]:
                heapq.heappush(heap, (neighbor_weight, neighbor, current_vertex))

    return mst


graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 1), ('D', 3)],
    'C': [('B', 1), ('D', 4)],
    'D': [('A', 5), ('B', 3), ('C', 4)]
