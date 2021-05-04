def solution(numbers, hand):
    answer = ''
    line = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}
    left, right = (3, 0), (3, 2)
    
    for number in numbers:
        if number in (1, 4, 7):
            left = line[number]
            answer += 'L'
        elif number in (3, 6, 9):
            right = line[number]
            answer += 'R'
        else:
            fr_left = abs(line[number][0] - left[0]) + abs(line[number][1] - left[1])
            fr_right = abs(line[number][0] - right[0]) + abs(line[number][1] - right[1])
            if fr_left < fr_right:
                left = line[number]
                answer += 'L'
            elif fr_left > fr_right:
                right = line[number]
                answer += 'R'
            else:
                if hand == 'left':
                    left = line[number]
                    answer += 'L'
                else:
                    right = line[number]
                    answer += 'R'
        
    return answer
