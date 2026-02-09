"""   
     02 / 09 / 26 - Count Nodes Greater Than X

Given a binary tree and an integer x,
return the number of nodes whose value is strictly greater than x.
"""

def countGreater(root, x):
    if root is None:
        return 0
    
    count = 0

    if root.val > x:
        count += 1

    return count + countGreater(root.left) + countGreater(root.right)
