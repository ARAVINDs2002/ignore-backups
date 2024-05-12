import heapq
from collections import defaultdict

class Node:
    def __init__(self, symbol=None, frequency=None, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(data):
    frequency_map = defaultdict(int)
    for symbol in data:
        frequency_map[symbol] += 1

    priority_queue = [Node(symbol, freq) for symbol, freq in frequency_map.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        internal_node = Node(frequency=left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]

def encode_data(root, data):
    if not root:
        return {}

    codes = {}

    def traverse(node, code):
        if node.symbol:
            codes[node.symbol] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    traverse(root, '')
    
    encoded_data = ''.join(codes[symbol] for symbol in data)
    
    return encoded_data, codes

def decode_data(root, encoded_data):
    if not root:
        return ''

    decoded_data = ''
    current_node = root

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.symbol:
            decoded_data += current_node.symbol
            current_node = root

    return decoded_data

# Example usage:
data = "Huffman is dead"
root = build_huffman_tree(data)
encoded_data, codes = encode_data(root, data)
decoded_data = decode_data(root, encoded_data)

print("Original data:", data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)
print("Codes:", codes)
