class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Functions for tree traversal
def preorderTraversal(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

def inorderTraversal(root):
    if not root:
        return []
    
    stack = []
    result = []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result

def postorderTraversal(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return result[::-1]

# Constructing the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Output of traversals
print("Preorder Traversal:", preorderTraversal(root))  # Output: [1, 2, 4, 5, 3]
print("Inorder Traversal:", inorderTraversal(root))    # Output: [4, 2, 5, 1, 3]
print("Postorder Traversal:", postorderTraversal(root))  # Output: [4, 5, 2, 3, 1]
