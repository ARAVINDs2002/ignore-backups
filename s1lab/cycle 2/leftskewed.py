class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_complete_tree(height):
    if height == 0:
        return None
    root = TreeNode(1)
    root.left = create_complete_tree(height - 1)
    root.right = create_complete_tree(height - 1)
    return root

def remove_right_subtree(node, depth):
    if node is None:
        return
    if depth == 0:
        node.right = None
    else:
        remove_right_subtree(node.right, depth - 1)

def create_left_skewed_tree(height):
    root = create_complete_tree(height)
    remove_right_subtree(root, height - 1)
    return root

def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    elif value > root.value:
        root.right = insert_into_bst(root.right, value)
    return root

def search_bst(root, target):
    comparisons = 0
    current = root
    while current is not None:
        comparisons += 1
        if target == current.value:
            return comparisons
        elif target < current.value:
            current = current.left
        else:
            current = current.right
    return comparisons

# Create a left-skewed binary tree with a minimum height of 4
left_skewed_tree = create_left_skewed_tree(4)

# Create a height-balanced binary search tree from the left-skewed tree
def balance_tree(root):
    if root is None:
        return None
    values = []
    inorder_traversal(root, values)
    return create_bst_from_sorted_array(values)

def inorder_traversal(root, values):
    if root is None:
        return
    inorder_traversal(root.left, values)
    values.append(root.value)
    inorder_traversal(root.right, values)

def create_bst_from_sorted_array(values):
    if not values:
        return None
    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = create_bst_from_sorted_array(values[:mid])
    root.right = create_bst_from_sorted_array(values[mid + 1:])
    return root

balanced_tree = balance_tree(left_skewed_tree)

# Search for two data in both trees and find the number of comparisons
data_to_search = [10, 15]

for data in data_to_search:
    comparisons_left_skewed_tree = search_bst(left_skewed_tree, data)
    comparisons_balanced_tree = search_bst(balanced_tree, data)
    print(f"Search for {data}:")
    print(f"Number of comparisons in left-skewed tree: {comparisons_left_skewed_tree}")
    print(f"Number of comparisons in height-balanced tree: {comparisons_balanced_tree}")
