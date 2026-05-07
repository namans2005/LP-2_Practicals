"""
Implement Greedy Search Algorithm for any application below:
SELECTION SORT
"""

arr = [34, 20, 3, 14]
print("original array:", arr)

def selec_sort(arr):
    n = len(arr)

    for i in range(n):
        mini = i

        for j in range(i+1, n):
            if arr[j] <= arr[mini]:
                mini = j
        
        arr[i], arr[mini] = arr[mini], arr[i]
        print("Iteration", i+1, "is", arr)

    return arr

sorted_arr = selec_sort(arr)
print("After sorting:", sorted_arr)


"""
Implement Greedy Search Algorithm for any application below:
PRIMS MST ALGORITHM
"""

import heapq

def prims_mst(graph, start=0):
    visited = set()
    min_heap = [(0, start, -1)]
    total_cost = 0
    mst_edges = []

    while min_heap and len(visited) < len(graph):
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue
        
        visited.add(node)
        total_cost += weight

        if parent != -1:
            mst_edges.append((parent, node, weight))

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, node))
        
    print("Edge \tWeight")
    for u,v,w in mst_edges:
        print(f"{u} - {v}\t{w}")
    
    print("Total cost:", total_cost)

