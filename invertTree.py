# Invert Binary Tree

# Given the root of a binary tree, invert the tree.

def invertTree(root):
    if root is None:
        return None
    
    root.left, root.right, = root.right, root.left
    
    invertTree(root.left)
    invertTree(root.right)

    return root