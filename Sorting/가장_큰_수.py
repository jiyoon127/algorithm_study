from functools import cmp_to_key

def comparator(a,b):
    n1 = a + b
    n2 = b + a
    return - (int(n1) < int(n2))

def solution(numbers):
    numbers = [str(number) for number in numbers]
    numbers.sort(key = cmp_to_key(comparator), reverse = True)
    
    return str(int(''.join(numbers)))
