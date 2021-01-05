# 2020 KAKAO BLIND RECRUITMENT 자물쇠와 
# https://programmers.co.kr/learn/courses/30/lessons/60059

def rotate_90(arr):
    n = len(arr)
    m = len(arr[0])
    result = [[0] * n for _ in range(m)]

    for r in range(n):
        for c in range(m):
            result[c][n-1-r] = arr[r][c]
    return result
    
def check(arr):
    length = len(arr) // 3
    for r in range(length, length * 2):
        for c in range(length, length * 2):
            if arr[r][c] != 1: return False
    return True
    
def solution(key, lock): 
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    for r in range(n):
        for c in range(n):
            new_lock[r + n][c + n] = lock[r][c]
    for _ in range(4):
        key = rotate_90(key)
        for r in range(n * 2):
            for c in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[r+i][c+j] += key[i][j]
                if check(new_lock) == True: return Trueㅇ
                for i in range(m):
                    for j in range(m):
                        new_lock[r+i][c+j] -= key[i][j]
        
    return False
