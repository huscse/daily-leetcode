"""
Plain BFS Traversal (No Levels)

First, forget grouping by levels.

Just return values in BFS order as a flat list.

"""

from collections import deque

def bfsTraversal(root):
    if root is None:
        return []
    
    result = []

    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result
