import heapq

def solution(operations):
    q = []

    for operation in operations:
        if operation[0] == 'I':
            num = int(operation[2:])
            heapq.heappush(q, num)
        elif q:
            if operation[2] == '1':
                q = heapq.nlargest(len(q), q)[1:]
                heapq.heapify(q)
            else:
                heapq.heappop(q)
    _max, _min = (heapq.nlargest(len(q), q)[0], heapq.heappop(q)) if len(q) >= 2 else (0, 0)
    return [_max, _min]
