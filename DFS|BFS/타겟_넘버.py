answer = 0
def add(i, _sum, numbers, target):
    global answer
    if i == len(numbers):
        if _sum == target: answer += 1
        return

    add(i + 1, _sum + numbers[i], numbers, target)
    add(i + 1, _sum - numbers[i], numbers, target)

def solution(numbers, target):
    add(0, 0, numbers, target)
    return answer
