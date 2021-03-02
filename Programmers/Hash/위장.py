def solution(clothes):

    C = {}
    
    for _,kind in clothes:
        C[kind] = 1

    for _,kind in clothes:
        C[kind] += 1

    answer = 1
    for n in C.values():
        answer *= n

    return answer - 1
