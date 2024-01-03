import heapq
from collections import defaultdict

def build_huffman_tree(frequencies):
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0][1:]

def huffman_encode(data):
    frequencies = defaultdict(int)
    for char in data:
        frequencies[char] += 1

    huffman_tree = build_huffman_tree(frequencies)
    encoded_data = ''.join([char[1] for char in huffman_tree])

    return encoded_data

def huffman_decode(encoded_data, huffman_tree):
    decoded_data = ""
    current_node = huffman_tree

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node[0]
        else:
            current_node = current_node[1]

        if type(current_node[0]) is str:
            decoded_data += current_node[0]
            current_node = huffman_tree

    return decoded_data

# Example usage:
input_data = "this is an example for huffman encoding"
encoded_data = huffman_encode(input_data)
print("Encoded data:", encoded_data)

decoded_data = huffman_decode(encoded_data, build_huffman_tree({char: encoded_data.count(char) for char in set(encoded_data)}))
print("Decoded data:", decoded_data)
