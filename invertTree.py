# Invert Binary Tree

# Given the root of a binary tree, invert the tree.

def invertTree(root):
    if root is None:
        return None
    
    root.left, root.right, = root.right, root.left
    
    invertTree(root.left)
    invertTree(root.right)

    return root


# Path Sum

# Given the root of a binary tree and an integer targetSum,
# return True if the tree has a root-to-leaf path such that:

def hasPathSum(root, targetSum):
    if root is None:
        return False
    
    diff = targetSum - root.val

    if root.left is None and root.right is None:
        return diff == 0
        

    return hasPathSum(root.left, diff) or hasPathSum(root.right, diff)


def countNodes(root):
    if root is None:
        return 0
    
    return 1 + countNodes(root.left) + countNodes(root.right)

def sumNodes(root):
    if root is None:
        return 0
    
    return root.val + sumNodes(root.left) + sumNodes(root.right)

def leafNodes(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    return leafNodes(root.left) + leafNodes(root.right)


def countSingleChild(root):
    if root is None:
        return 0
    
    count = 0

    if (root.left is None and root.right is not None) or \
       (root.left is not None and root.right is None):
        count = 1
    
    return count + countSingleChild(root.left) + countSingleChild(root.right)

  




    