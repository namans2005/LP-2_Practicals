graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

visited = []
def dfs(v):
    if v not in visited:
        print(v, end=" ")
        visited.append(v)
        for i in graph[v]:
            dfs(i)
dfs('A')
print("\n")



def bfs(v):
    visited = [v]
    queue = [v]
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
bfs('A')