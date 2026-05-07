"""
Implement A* algoritm for any game search problem.
"""

import heapq

def a_star(graph, start, goal, heuristic):
    open_list = [(0, start)]
    g_cost = {start : 0}
    parent = {start: None}

    while open_list:
        _, node = heapq.heappop(open_list)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            path = path[::-1]
            return path, g_cost[goal]
    
        for neighbor, cost in graph[node]:
            new_cost = g_cost[node] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = node
    
    return None

graph = {
'S':[('A',2), ('B',5)],
'A':[('C',4)],
'B':[('C',1)],
'C':[('G',3)],
'G':[]
}

heuristic = {
'S':7, 'A':4, 'B':2, 'C':1, 'G':0
}

path, cost = a_star(graph, 'S', 'G', heuristic)
print(path)
print(cost)