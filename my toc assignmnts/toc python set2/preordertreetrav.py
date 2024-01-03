class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preorder_non_recursive(root):
    stack = []
    current = root

    while current or stack:
        # Visit the current node
        while current:
            print(current.data, end="->")
            stack.append(current)
            current = current.left

        # Move to the right subtree
        current = stack.pop()
        current = current.right

# Example usage:
# Assuming you have a binary tree with values [1, 2, 3, 4, 5]
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)

print("Preorder traversal (non-recursive):")
preorder_non_recursive(root)
print("null")
