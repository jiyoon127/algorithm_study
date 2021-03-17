from collections import deque
n, l = map(int, input().split())
data = list(map(int, input().split()))

q = deque()

for i, num in enumerate(data):
    while q and q[-1] > num: q.pop()
    q.append(num)

    if i >= l and q[0] == data[i - l]: q.popleft()

    print(q[0], end=' ')
