import re
answer = 0

def calculate(cnt, opers, visited, cur):
    global answer

    if cnt == len(opers):
        answer = max(answer, abs(int(cur[0])))
        return

    for i, oper in enumerate(opers):
        if visited[i]: continue
        visited[i] = 1
        new_cur = cur
        while oper in new_cur:
            idx = new_cur.index(oper)
            new_cur = new_cur[:idx - 1] + [str(eval(''.join(new_cur[idx - 1:idx + 2])))] + new_cur[idx + 2:]
        calculate(cnt + 1, opers, visited, new_cur)
        visited[i] = 0


def solution(expression):
    opers = set(re.findall('[^\d]', expression))
    visited = [0] * len(opers)
    cur = re.split('(\D)', expression)

    calculate(0, opers, visited, cur)
    return answer
