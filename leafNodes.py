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