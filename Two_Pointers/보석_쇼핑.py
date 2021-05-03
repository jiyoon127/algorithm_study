from collections import defaultdict

def solution(gems):
    answer = [0, len(gems)]
    
    kinds = len(set(gems))
    cur_dict = defaultdict(int)
    if kinds == 1: return [1, 1]
    
    cur_dict[gems[0]] = 1
    end = 0
    for start in range(len(gems)):
        while len(cur_dict) != kinds:
            end += 1
            if end == len(gems): return answer
            cur_dict[gems[end]] += 1
            
        if end - start < answer[1] - answer[0]: answer = [start + 1, end + 1]
            
        cur_dict[gems[start]] -= 1
        if not cur_dict[gems[start]]: del cur_dict[gems[start]]
