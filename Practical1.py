"""
Implement depth first search algorithm and Breadth First Search
algorithm, use an undirected graph and develop a recursive algorithm
for searching all the vertices of a graph or tree data structure.
"""

graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['E', 'F'],
    'C' : ['G', 'H'],
    'D' : ['J'],
    'E' : [],
    'F' : [],
    'G' : [],
    'H' : [],
    'J' : []
}

def bfs(visit_comp, graph, cur_node):
    visit_comp = []
    visit_comp.append(cur_node)
    queue = []
    queue.append(cur_node)

    while queue:
        t = queue.pop(0)
        print(t, end=" ")

        for neighbor in graph[t]:
            if neighbor not in visit_comp:
                visit_comp.append(neighbor)
                queue.append(neighbor)

def dfs(visit_comp, graph, cur_node):
    stack = []
    stack.append(cur_node)

    while  stack:
        s = stack.pop()
        if s not in visit_comp:
            visit_comp.append(s)
            print(s, end= " ")

            for neighbor in reversed(graph[s]):
                stack.append(neighbor)

bfs([], graph, 'A')
print()
dfs([], graph, 'A')
print()
