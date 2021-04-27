def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    grades = [0] * 3

    for i, answer in enumerate(answers):
        if answer == a1[i % len(a1)]: grades[0] += 1
        if answer == a2[i % len(a2)]: grades[1] += 1
        if answer == a3[i % len(a3)]: grades[2] += 1
        
    _max = max(grades)
    answer = [i + 1 for i, v in enumerate(grades) if v == _max]
    
    return answer
