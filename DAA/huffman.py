import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char          # character
        self.freq = freq          # frequency
        self.left = None          # left child
        self.right = None         # right child

    # define comparison for heapq
    def __lt__(self, other):
        return self.freq < other.freq


# Function to print Huffman codes (recursive traversal)
def print_codes(root, code=""):
    if root is None:
        return

    # Leaf node → print character and code
    if root.left is None and root.right is None:
        print(f"{root.char}: {code}")
        return

    print_codes(root.left, code + "0")
    print_codes(root.right, code + "1")


# Function to build Huffman Tree
def build_huffman_tree(chars, freqs):
    heap = []

    # Step 1: Create leaf nodes for each character and push into heap
    for i in range(len(chars)):
        heapq.heappush(heap, Node(chars[i], freqs[i]))

    # Step 2: Repeat until only one node remains (root)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create internal node with combined frequency
        parent = Node('$', left.freq + right.freq)
        parent.left = left
        parent.right = right

        heapq.heappush(heap, parent)

    # The remaining node is the root of the Huffman Tree
    return heap[0]


chars = ['A', 'B', 'C', 'D', 'E', 'F']
freqs = [5, 9, 12, 13, 16, 45]

root = build_huffman_tree(chars, freqs)

print("Huffman Codes:")
print_codes(root)
print(root)
