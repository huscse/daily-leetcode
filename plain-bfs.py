"""
    02/14/2026 - BFS, level-order BFS
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


def levelOrder(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


        