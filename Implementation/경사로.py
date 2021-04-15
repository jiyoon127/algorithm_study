import sys
input = sys.stdin.readline

def turn():
    new_board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[i][j] = board[j][i]
    return new_board

def findAvailable(board):
    global ans

    for row in board:
        prev_i, cur_i = 0, 1
        lamp = [False] * n
        is_possible = True
        while cur_i < n:
            if row[cur_i] == row[prev_i]: # 같은 높이
                prev_i += 1
                cur_i += 1
                continue
            elif abs(row[cur_i] - row[prev_i]) > 1:
                is_possible = False
                break # 높이 2 이상 차이

            if row[cur_i] > row[prev_i] and cur_i - l >= 0: # 오른쪽이 높을 경우
                for i in range(cur_i - l, cur_i):
                    if row[i] != row[prev_i] or lamp[i]:
                        is_possible = False
                        break
                    else: lamp[i] = True
                prev_i = cur_i
                cur_i += 1

            elif row[cur_i] < row[prev_i] and prev_i + l < n: # 왼쪽이 높을 경우
                for i in range(prev_i + 1, prev_i + l + 1):
                    if row[i] != row[cur_i] or lamp[i]:
                        is_possible = False
                        break
                    else: lamp[i] = True

                prev_i += l
                cur_i = prev_i + 1

            else: is_possible = False

            if not is_possible:
                break # 못 놓을 경우 다음줄 탐색

        if is_possible: ans += 1

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for cnt in range(2):
    findAvailable(board)
    if not cnt:
        board = turn()

print(ans)
