answer = []

def dfs(ticket, tickets, visited, path):
    global answer
    
    fr, to = ticket
    
    if len(path) == len(tickets) + 1: 
        cur = list(to for fr, to in path)
        if answer:
            for ans, _new in zip(answer, cur):
                if ans < _new: break
                elif ans > _new:
                    answer = cur
                    break
            
        else: answer = cur
        return
    
    for i, ticket in enumerate(tickets):
        if to == ticket[0] and not visited[i]:
            visited[i] = 1
            path.append(ticket)
            dfs(ticket, tickets, visited, path)
            path.pop()
            visited[i] = 0
    

def solution(tickets):
    visited = [0] * len(tickets)
    
    dfs(["", "ICN"], tickets, visited, [["", "ICN"]])
    
    return answer
