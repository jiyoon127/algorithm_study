def solution(name):
    answer = 0
    name = [*name]

    i, changed = 0, 0
    
    while True:
        target = ord(name[i])
        if target - 65 <= 90 - target: answer += target - 65
        else: answer += 90 - target + 1

        name[i] = 'A'

        if all(ch == 'A' for ch in name): break

        left, right = 1, 1
        while name[i - left] == 'A': left += 1
        while name[(i + right) % len(name)] == 'A': right += 1
        answer += min(left, right)
        i += -left if left < right else right

        changed += 1

    return answer
