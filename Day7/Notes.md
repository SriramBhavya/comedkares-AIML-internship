Greedy Best-First Search is an informed search algorithm that expands the node that appears closest to the goal, using a heuristic function h(n).
Formula:
f(n) = h(n)
h(n) = estimated cost from node n to the goal
It chooses the node with the lowest h(n).
It is generally faster than uninformed search, but does not always find the shortest path
