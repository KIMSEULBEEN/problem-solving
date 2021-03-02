def solution(phone_book):
    phone_book = sorted(phone_book)

    len_pb = len(phone_book)
    for n in range(len_pb-1):
        len_tmp = len(phone_book[n])
        for m in range(n+1,len_pb):
            if phone_book[m].startswith(phone_book[n]):
                return False
   
    return True
