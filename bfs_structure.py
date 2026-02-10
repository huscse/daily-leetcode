# BFS - list of levels

from collections import deque  # We use deque because it supports fast pop from left (O(1))

def levelOrder(root):
    # If the tree is empty, there are no levels
    if root is None:
        return []

    result = []  # This will store our final answer (list of levels)

    # Initialize queue with the root node
    # The queue represents nodes waiting to be processed
    queue = deque([root])

    # Continue until there are no more nodes to process
    while queue:

        level = []  # This will store values for the current level

        # Capture how many nodes are currently in this level
        # IMPORTANT: This freezes the boundary of the level
        level_size = len(queue)

        # Process exactly 'level_size' nodes
        # We use "_" because we don't need the loop variable
        for _ in range(level_size):

            # Remove node from front of queue (FIFO)
            node = queue.popleft()

            # Add the node's value to the current level list
            level.append(node.val)

            # If left child exists, add it to the queue
            # It will be processed in the next level
            if node.left:
                queue.append(node.left)

            # If right child exists, add it to the queue
            if node.right:
                queue.append(node.right)

        # After processing this level completely,
        # add the level list to the result
        result.append(level)

    # Once the queue is empty, we've processed all levels
    return result
