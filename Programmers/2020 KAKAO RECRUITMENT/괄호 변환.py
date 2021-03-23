def solution(P):
    # 1. u, v 나누기
    a,a_flag = 0, True

    n = 0
    for n in range(len(P)):
        p = P[n]
        a = a + 1 if p == '(' else a - 1
        if a < 0: a_flag = False
        if a == 0: break

    u, v = P[:n + 1], P[n + 1:]
    #  1-1. v 크기 0일 경우 (입력 반환)
    if len(v) == 0 and a_flag: answer = P
    #  1-2. v 크기 0이 아닐 경우
    else:
        # a) u가 올바른 괄호 문자열일 경우
        if a_flag: answer = u + solution(v)

        # b) u가 올바른 괄호 문자열이 아닐 경우
        else:
            answer = '(' + solution(v) + ')'
            for t in range(1,len(u) - 1):
                answer = answer + ')' if u[t] == '(' else answer + '('

    return answer
