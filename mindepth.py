""""
    02 / 16 / 2026 - Minimum Depth (BFS version)
    Goes level by level
"""

from collections import deque

def minDepth(root):
    if root is None:
        return 0  # Empty tree has depth 0
    
    queue = deque([root])  # Start BFS with root in queue
    depth = 0              # Tracks current level (depth)

    while queue:           # Continue while there are nodes to process
        depth += 1         # We are moving to the next level
        
        # Process all nodes currently in this level
        for _ in range(len(queue)):
            node = queue.popleft()  # Remove front node (FIFO)

            # If this node is a leaf, we've found minimum depth
            if node.left is None and node.right is None:
                return depth
        
            # Add children to queue for next level
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)