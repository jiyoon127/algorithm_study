def solution(tickets):
    routes = {}

    for fr, to in tickets:
        routes[fr] = routes.get(fr, []) + [to]  

    for r in routes:
        routes[r].sort(reverse = True)

    stack = ["ICN"]
    path = []
    
    while stack:
        cur = stack[-1]

        if cur in routes and routes[cur]: stack.append(routes[cur].pop())
        else: path.append(stack.pop())
        print(stack)
    return path[:: -1]
