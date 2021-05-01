def solution(array, commands):
    answer = []
    
    for i, command in enumerate(commands):
        start, end, target = command
        tmp = array[start - 1 : end]
        answer.append(sorted(tmp)[target - 1])
        
    return answer
