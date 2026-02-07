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