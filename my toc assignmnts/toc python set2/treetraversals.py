class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_non_recursive(root):
    stack = []
    current = root

    while current or stack:
        # Traverse to the leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Visit the top of the stack
        current = stack.pop()
        print(current.data, end="->")

        # Move to the right subtree
        current = current.right

# Creating a sample binary tree
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)

# Performing inorder traversal
print("Inorder traversal (non-recursive):")
inorder_non_recursive(root)
print("null")
