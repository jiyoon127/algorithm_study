from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n)]
    dist = [0] * n
    visited = [0] * n
    for x, y in edge:
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)

    q = deque()
    q.append(0)
    visited[0], dist[0] = 1, 0
    
    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                visited[node] = 1

                dist[node] = dist[now] + 1
                q.append(node)
    
    _max = max(dist)
    return dist.count(_max)
