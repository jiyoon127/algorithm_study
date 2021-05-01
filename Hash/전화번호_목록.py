def solution(phone_book):
    
    phone_book.sort(key = int)
    dict = {phone: 1 for phone in phone_book}

    for phone in phone_book:
        for i in range(len(phone)):
            if phone[:i + 1] in dict and phone[:i + 1] != phone: return False
            
    return True
