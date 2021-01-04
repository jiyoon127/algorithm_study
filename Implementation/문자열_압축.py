# programmers 2020 KAKAO BLIND RECRUITMENT 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    word = ''
    for step in range(1, len(s) // 2 + 1):
        newStr = ''
        prev = s[0:step]
        cnt = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]: cnt += 1
            else: 
                newStr += str(cnt) + prev if cnt >= 2 else prev
                cnt = 1
                prev = s[j:j + step]
        newStr += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(newStr))
            
    return answer
