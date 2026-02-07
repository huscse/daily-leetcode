"""
    02 / 07 / 2026 - Count leaf nodes

🌳 Problem 2: Count Leaf Nodes

A leaf is a node with:

no left child

no right child

Return the number of leaf nodes in the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countLeaves(root):
    if root is None:
        return 0
    
    # leaf check
    if root.left is None and root.right is None:
        return 1
    
    return countLeaves(root.left) + countLeaves(root.right)


def contains(root, target):
    if root is None:
        return False
    
    if root.val == target:
        return True
    
    return contains(root.left, target) or contains(root.right, target)



