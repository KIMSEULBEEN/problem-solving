def solution(answers):
    answer = []

    arr_supo = [[1,2,3,4,5],
                [2,1,2,3,2,4,2,5],
                [3,3,1,1,2,2,4,4,5,5]]

    sum_supo = [0,0,0]

    num_supo = [5,8,10]

    len_answers = len(answers)
    for n in range(len_answers):
        for m in range(3):
            idx =  n % num_supo[m] 
            if answers[n] == arr_supo[m][idx]:
                sum_supo[m] += 1

    max_sum = max(sum_supo)
    for n in range(3):
        if sum_supo[n] == max_sum:
            answer.append(n+1)

    return answer
