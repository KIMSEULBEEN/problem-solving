def solution(str1, str2):

    # 1) Make small letters
    str1 = str1.lower()
    str2 = str2.lower()

    # 2) A,B
    A,B = [],[]

    len_str1,len_str2 = len(str1),len(str2)


    for x in range(len_str1):
        if 'a' <= str1[x] and str1[x] <= 'z':
            if x != len_str1 -1 and 'a' <= str1[x+1] and str1[x+1] <= 'z':
                A.append(str1[x:x+2])



    for x in range(len_str2):
        if 'a' <= str2[x] and str2[x] <= 'z':
            if x != len_str2 -1 and 'a' <= str2[x+1] and str2[x+1] <= 'z':
                B.append(str2[x:x+2])



    ###
    print(A)
    print(B)
    ###

    # 4) Considering overlap & J(A,B)

    AiB = set(A)&set(B)
    AuB = set(A)|set(B)

    AiB = sorted(list(AiB))
    AuB = sorted(list(AuB))
    
    
    ###
    print(AiB)
    print(AuB)
    ###

    # Considering overlap
    co_i,co_u = 0,0
    for x in AiB:
        no_a = A.count(x)
        no_b = B.count(x)

        co_i += min(no_a,no_b) -1
        # co_u += max(no_a,no_b) -1

    for x in AuB:
        no_a = A.count(x)
        no_b = B.count(x)

        # co_i += min(no_a,no_b) -1
        co_u += max(no_a,no_b) -1

    ###
    print(len(AiB) + co_i)
    print(len(AuB) + co_u)
    ###
    if len(A) == 0 and len(B) == 0:
        answer = 65536
    else:
        answer = (len(AiB) + co_i)/(len(AuB) + co_u)
        answer = int(answer*65536)

    ###
    print(co_i,co_u)
    print(answer)
    ###

    return answer
