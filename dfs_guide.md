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

Add its children to the queue.

-- Graphs are stored in two common ways:

1. Adjacency List: Example graph:

A — B
| |
C — D

Representation:

A: B, C
B: A, D
C: A, D
D: B, C

2.  Adjacency Matrix: Table of connections

        A B C D

    A 0 1 1 0
    B 1 0 0 1
    C 1 0 0 1
    D 0 1 1 0

1 -> an edge exists

Depth First Search (DFS) on graphs

DFS is used to: find connected components
detect cycles
explore graphs

Idea: 

1. Start at a vertex
2. Visit one neighbor
3. Keep going deeper
4. Backtrack when stuck

Pseudo:

v is given vertex
DFS(v):
    mark v as visited
    for each neighbor vertex u of v:
        if u not visited:
            DFS(u)

--> We mark nodes as visited so we don't revisit them
 
DFS runs in O(V + E) where 

V = number of vertices
E = number of edges

In undirected graphs you can go both ways but 
in directed graphs you can go A → B, but not B → A unless there is another arrow