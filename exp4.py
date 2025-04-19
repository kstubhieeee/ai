import heapq

class Node:
    def __init__(self, x, y, g_cost, h_cost):
        self.x = x
        self.y = y
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parents = []

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def backtrack_paths(node):
    if not node.parents:
        return [[(node.x, node.y)]]
    paths = []
    for parent in node.parents:
        for path in backtrack_paths(parent):
            paths.append(path + [(node.x, node.y)])
    return paths

def a_star_search(maze, start, goal, heuristics):
    open_list = []
    node_map = {}
    start_node = Node(start[0], start[1], 0, heuristics[start])
    node_map[(start[0], start[1])] = start_node
    heapq.heappush(open_list, start_node)

    directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]

    while open_list:
        current = heapq.heappop(open_list)
        x, y = current.x, current.y

        if (x, y) == goal:
            return backtrack_paths(current)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                new_g = current.g_cost + 1
                h = heuristics.get((nx, ny), float('inf'))
                new_f = new_g + h

                if (nx, ny) not in node_map:
                    neighbor = Node(nx, ny, new_g, h)
                    neighbor.parents.append(current)
                    node_map[(nx, ny)] = neighbor
                    heapq.heappush(open_list, neighbor)
                else:
                    neighbor = node_map[(nx, ny)]
                    if new_g < neighbor.g_cost - 1e-6:
                        neighbor.g_cost = new_g
                        neighbor.h_cost = h
                        neighbor.f_cost = new_f
                        neighbor.parents = [current]
                        heapq.heappush(open_list, neighbor)
                    elif abs(new_g - neighbor.g_cost) < 1e-6:
                        neighbor.parents.append(current)
    return None

# Example usage
maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

heuristics = {
    (0, 0): 6, (0, 1): 5, (0, 2): 4, (0, 3): float('inf'), (0, 4): 3,
    (1, 0): float('inf'), (1, 1): float('inf'), (1, 2): 3, (1, 3): float('inf'), (1, 4): 2,
    (2, 0): 4, (2, 1): 3, (2, 2): 2, (2, 3): 1, (2, 4): 0,
    (3, 0): 3, (3, 1): float('inf'), (3, 2): float('inf'), (3, 3): float('inf'), (3, 4): 1,
    (4, 0): 2, (4, 1): 1, (4, 2): 0, (4, 3): 1, (4, 4): 0
}

start = (0, 0)
goal = (4, 4)

paths = a_star_search(maze, start, goal, heuristics)

if paths:
    print("Paths found:")
    for path in paths:
        print(path)
else:
    print("No path found!")
