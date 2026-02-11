from collections import deque
def solution(phone_book):
    phone_book_sorted = deque(sorted(phone_book))
    while phone_book_sorted:
        temp = phone_book_sorted.popleft()
        if phone_book_sorted[0].startswith(temp):
            return False
        if len(phone_book_sorted) == 1:
            break
        
            
    return True
            