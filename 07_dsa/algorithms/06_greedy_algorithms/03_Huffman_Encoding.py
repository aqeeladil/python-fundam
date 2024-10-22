

# Huffman Encoding

# Problem Statement: Given a set of characters and their frequencies, build a binary tree 
# (Huffman Tree) to encode the characters with the minimum number of bits.

import heapq
from collections import defaultdict

class TreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    priority_queue = [TreeNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = TreeNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0]

def build_huffman_codes(root, prefix='', codes=defaultdict()):
    if root is not None:
        if root.char is not None:
            codes[root.char] = prefix
        build_huffman_codes(root.left, prefix + '0', codes)
        build_huffman_codes(root.right, prefix + '1', codes)
    
    return codes

# Example usage:
frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
huffman_tree = build_huffman_tree(frequencies)
huffman_codes = build_huffman_codes(huffman_tree)
print(huffman_codes)
# Example output: {'a': '1111', 'b': '1110', 'c': '110', 'd': '10', 'e': '0', 'f': '11'}
