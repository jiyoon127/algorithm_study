import heapq

def solution(scoville, k):
    answer = 0
    q = [*scoville]
    heapq.heapify(q)

    while q[0] < k:
        if len(q) > 1:
            first, second = heapq.heappop(q), heapq.heappop(q)
            _new = first + 2 * second
            heapq.heappush(q, _new)
            answer += 1
        else: return -1
    return answer
