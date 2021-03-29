def solution(N, stages):
    tn = len(stages)

    answer = []
    FR = []
    for n in range(1,N+1):

        cn = stages.count(n)
        tn -= stages.count(n-1)
        if cn == 0:
            FR.append(0)
        else:
            FR.append(cn/tn)

    print(FR)
    FR_2 = []
    FR_2.append(FR)
    FR_2.append(list(range(1,N+1)))

    for n in range(N):
        maxidx = FR_2[0].index(max(FR_2[0]))
        FR_2[0].pop(maxidx)
        tmp = FR_2[1].pop(maxidx)

        answer.append(tmp)

    return answer
