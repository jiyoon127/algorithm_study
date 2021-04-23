def solution(brown, yellow):
    answer = []
    brown += 4
    brown //= 2

    column = brown // 2
    row = brown - column

    while True:
        if column < 3: break
        if (row - 2) * (column - 2) == yellow: 
            answer = [row, column]
            break

        row += 1
        column -= 1

    return answer
