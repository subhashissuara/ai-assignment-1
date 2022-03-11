# --------------------------
#   Author: Subhashis Suara
#   Roll No.: UCSE19012
# --------------------------

def uniform_cost_search(graph, cost, start, goal):
    """
    Returns the minimum cost path from start to goal
    """
    result = []
    visited = {}
    count = 0
    # Priority queue
    priority_queue = []

    # Set the result vector to max value
    for i in range(len(goal)):
        result.append(10**8)

    # Insert the starting index
    priority_queue.append([0, start])

    # While the priority queue is not empty
    while (len(priority_queue) > 0):
        # Top element of the sorted priority queue
        priority_queue = sorted(priority_queue)
        p = priority_queue[-1]

        del priority_queue[-1]

        # Original value
        p[0] *= -1

        # Check if the element in goal list
        if (p[1] in goal):
            index = goal.index(p[1])

            # If a new goal is reached
            if (result[index] == 10**8):
                count += 1

            # If the cost is less
            if (result[index] > p[0]):
                result[index] = p[0]

            del priority_queue[-1]

            priority_queue = sorted(priority_queue)
            if (count == len(goal)):
                return result

        # Check for the non visited nodes which are adjacent to present node
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):
                # Value is multiplied by -1 so that least priority is at the top
                priority_queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])

        # Mark as visited
        visited[p[1]] = 1

    return result

if __name__ == '__main__':
    graph = [[] for i in range(8)]
    cost = {}
    goal = []
    start_value = 0
    goal_value = 4

    goal.append(goal_value)

    # Add edges to the graph
    graph[0].append(1)
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(6)
    graph[3].append(4)
    graph[1].append(6)
    graph[4].append(2)
    graph[4].append(5)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)

    # Add the cost of edges
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7

    result = uniform_cost_search(graph, cost, start_value, goal)
    print(f"Minimum cost from {start_value} to {goal_value}: ", result[0])