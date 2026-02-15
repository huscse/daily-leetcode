DFS:

Time → O(n)

Space → O(height)

BFS:

Time → O(n)

Space → O(width) → worst case O(n)

# We use BFS when we care about:

## Levels

## Shortest path (in graphs)

## Minimum steps

## Layered structure

# BFS uses a queue.

Why?

Because a queue is:

First In, First Out (FIFO).

# 🧩 Core BFS Mechanism

We:

Put root into a queue.

While queue is not empty:

Take node from front

Process it

Add its children to the queue
