# programmers 2019 KAKAO BLIND RECRUITMENT 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

import heapq
def solution(food_times, k):
    if sum(food_times) <= k: return -1
    
    ate, prev = 0, 0
    food_kind = len(food_times)
    q = []

    for i in range(food_kind):
        heapq.heappush(q, (food_times[i], i+1))
    while ate + (q[0][0] - prev) * food_kind <= k:
        now = heapq.heappop(q)[0]
        ate += (now - prev) * food_kind
        food_kind -= 1
        prev = now
    
    q.sort(key = lambda x:x[1])
    return q[(k-ate) % food_kind][1]
