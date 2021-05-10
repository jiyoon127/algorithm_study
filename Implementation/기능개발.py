def solution(progresses, speeds):
    answer = []
    cur_max = 0
    
    for progress, speed in zip(progresses, speeds):
        need, extra = divmod((100 - progress), speed)
        if extra: need += 1
        
        if cur_max < need: 
            cur_max = need
            answer.append(1)
        else: answer[-1] += 1
    return answer
