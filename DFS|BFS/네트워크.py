def dfs(node, visited, computers):
    visited[node] = 1
    for _next in range(len(visited)):
        if _next != node and computers[node][_next] and not visited[_next]:
            dfs(_next, visited, computers)

        
def solution(n, computers):
    answer = 0
    visited = [0] * len(computers)
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(i, visited, computers)
            answer += 1
    return answer
