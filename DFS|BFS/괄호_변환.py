# PROGRAMMERS 2020 KAKAO BLIND RECRUITMENT 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058 

def balanced(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else: count -= 1
        if count == 0: return i

def isPerfect(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            if count == 0: return False
            count -= 1
    return True
    
def solution(p):
    answer = ''
    if p == '': return answer
    index = balanced(p)
    u = p[0 : index + 1]
    v = p[index + 1 : ]
    if isPerfect(u): answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)+")"
        u = list(u[1 : -1])
        for i in range(len(u)):
            if u[i] == "(": u[i] = ")"
            else: u[i] = "("
        answer += ''.join(u)
    return answer
