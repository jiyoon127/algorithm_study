from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque([(p, i) for i, p in enumerate(priorities)])
    cnt = 1
    
    while q:
        val, i = q.popleft()
        # if q and max(q, key = lambda x: x[0])[0] > val: q.append((val, i))
        if any(p[0] > val for p in q): q.append((val, i))
        elif i == location: return cnt
        else: cnt += 1
    
    return answer
