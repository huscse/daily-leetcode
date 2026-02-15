"""
    02/14/2026 - BFS
"""

from collections import deque

def bfs(root):
    if root is None:
        return []
    
    result = []
    
    queue = deque([root])

    while queue:
        node = queue.popleft()
        # process node here
        result.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result

        