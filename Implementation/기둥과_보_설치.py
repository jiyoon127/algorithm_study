# PROGRAMMERS 2020 KAKAO BLIND RECRUITMENT 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3

def possible(answer):
    for (x, y, a) in answer:
        if a == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        if a == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True
        
def solution(n, build_frame):
    answer = []
    for (x, y, a, b) in build_frame:
        if b == 0:
            answer.remove([x, y, a])
            if not possible(answer): answer.append([x, y, a])
        if b == 1:
            answer.append([x, y, a])
            if not possible(answer): answer.remove([x, y, a])
    return sorted(answer)
