class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder_non_recursive(root):
    stack = []
    result = []

    if not root:
        return result

    stack.append(root)

    while stack:
        current = stack.pop()
        result.append(current.data)

        # Note: Push left child first, so it gets processed after the right child
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    # Reverse the result to get the postorder traversal
    result.reverse()
    return result

# Example usage:
# Assuming you have a binary tree with values [1, 2, 3, 4, 5]
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)

print("Postorder traversal (non-recursive):")
result = postorder_non_recursive(root)
print("->".join(map(str, result)), end="->null\n")
