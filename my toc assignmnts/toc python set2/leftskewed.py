class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Manual insertion into left-skewed binary tree
left_skewed_root = TreeNode(1)
left_skewed_root.left = TreeNode(2)
left_skewed_root.left.left = TreeNode(3)
left_skewed_root.left.left.left = TreeNode(4)

# Transform into a height-balanced tree
elements = []

def extract_elements(root):
    if root is not None:
        extract_elements(root.left)
        elements.append(root.key)
        extract_elements(root.right)

extract_elements(left_skewed_root)

def create_balanced_tree(elements):
    if not elements:
        return None

    mid = len(elements) // 2
    root = TreeNode(elements[mid])
    root.left = create_balanced_tree(elements[:mid])
    root.right = create_balanced_tree(elements[mid + 1:])
    return root

balanced_root = create_balanced_tree(elements)

# Search for values in both trees
search_value_1 = 2
search_value_2 = 5

# Search in the left-skewed binary tree
comparisons_left_skewed = 0
current_node = left_skewed_root
while current_node is not None:
    comparisons_left_skewed += 1
    if search_value_1 == current_node.key or search_value_2 == current_node.key:
        break
    elif search_value_1 < current_node.key:
        current_node = current_node.left
    else:
        current_node = current_node.right

# Search in the height-balanced tree
comparisons_balanced = 0
current_node = balanced_root
while current_node is not None:
    comparisons_balanced += 1
    if search_value_1 == current_node.key or search_value_2 == current_node.key:
        break
    elif search_value_1 < current_node.key:
        current_node = current_node.left
    else:
        current_node = current_node.right

# Display results
print("Left-skewed binary tree comparisons:", comparisons_left_skewed)
print("Height-balanced tree comparisons:", comparisons_balanced)
