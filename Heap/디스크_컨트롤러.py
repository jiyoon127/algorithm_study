import heapq

def solution(jobs):
    answer, now, cnt = 0, 0, 0
    prev_start = -1
    q = []

    while cnt < len(jobs):
        for start, period in jobs:
            if prev_start < start <= now: heapq.heappush(q, [period, start])
        
        if q:
            cur_period, cur_start = heapq.heappop(q)
            prev_start = now
            now += cur_period
            answer += now - cur_start
            cnt += 1
            
        else: now += 1

    return answer // len(jobs)
