from collections import deque
from collections import defaultdict

def solution(arrows):
    answer = 0
    directs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    visited = defaultdict(int)
    paths = defaultdict(int)

    now = (0, 0)
    q = deque(now)
    for arrow in arrows:
        dx, dy = directs[arrow]
        for _ in range(2):
            next = (now[0] + dx, now[1] + dy)
            q.append(next)
            now = next

    fr = q.popleft()
    visited[fr] = 1
    while q:
        to = q.popleft()
        if visited[to] == 1:
            if not paths[(fr, to)]: answer += 1
        else: visited[to] = 1

        paths[(fr, to)] = 1
        paths[(to, fr)] = 1
        fr = to

    return answer
