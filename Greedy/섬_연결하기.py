def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

def solution(n, costs):
    answer = 0
    parent = [0] * (len(costs) + 1)
    edges = []
    
    for i in range(1, len(costs) + 1): parent[i] = i 
    for i, j, cost in costs: edges.append((cost, i, j))

    edges.sort()
    
    for edge in edges:
        cost, a, b = edge
        if findParent(parent, a) != findParent(parent, b):
            unionParent(parent, a, b)
            answer += cost
    
    return answer
