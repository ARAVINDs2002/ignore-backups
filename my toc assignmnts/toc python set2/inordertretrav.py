class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_non_recursive(root):
    stack = []
    current = root

    while current or stack:

        while current:
            stack.append(current)
            current = current.left


        current = stack.pop()
        print(current.data, end="->")


        current = current.right

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)


print("Inorder traversal (non-recursive):")
inorder_non_recursive(root)
print("null")
