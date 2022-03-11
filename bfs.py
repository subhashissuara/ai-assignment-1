# --------------------------
#   Author: Subhashis Suara
#   Roll No.: UCSE19012
# --------------------------

import collections

def bfs(graph, root):
    """
    Prints the BFS traversal of a graph
    """
    queue = collections.deque([root])
    visited = set()

    # Add the root to the visited set initally
    visited.add(root)

    print("Breadth First Traversal of Given Graph: ")

    # While the queue is not empty
    while queue:
        # Pick a vertex from queue
        vertex = queue.popleft()
        print(vertex, end=" ")

        # If not visited, mark it as visited, and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    bfs(graph, 2)