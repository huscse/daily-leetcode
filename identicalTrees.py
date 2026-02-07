"""   
     02 / 07 / 26 - Same TREE

Two binary trees are given.
Return True if they are identical.

Two trees are identical if:

They have the same structure

All corresponding nodes have the same value

"""


def isSameTree(p, q):
    # If both are null
    if p is None and q is None:
        return True
    
    if p is None or q is None:
        return False
    
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Time: O(n)
# Space: O(h)

# Symmetric tree:

# def isSymmetric(root):
#     if root is None:
#         return True
    
#     def isMirror(left, right):
#         if left is None and right is None:
#             return True
        
#         if left is None or right is None:
#             return False
        
#         if left.val != right.val:
#             return False
        
#         return(isMirror(left.left, right.right) and isMirror(left.right, right.left))
    
#     return isMirror(root.left, root.right)


# # Given the root of a binary tree, return its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root down to a leaf.


# idea: -> look at the left and right subtrees, stop when you can't go down further, every time we can still go further down, we add 1
# Take the max of both paths that we went

def maxDepth(root):
    if root is None:
        return 0
    
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)

    return 1 + max(leftDepth, rightDepth)

def minDepth(root):
    if root is None:
        return 0
    
    leftDepth = minDepth(root.left)
    rightDepth = minDepth(root.right)
    
    if root.left is None:
        return 1 + rightDepth
    
    if root.right is None:
        return 1 + leftDepth
    
    return 1 + min(leftDepth, rightDepth)