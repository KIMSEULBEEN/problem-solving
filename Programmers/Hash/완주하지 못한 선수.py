def solution(participant, completion):

    answer = set(participant) - set(completion)

    if len(answer) == 0:
        participant = sorted(participant)
        completion = sorted(completion)

        len_comp = len(completion)
        for i in range(len_comp):
            if participant[i] != completion[i] or i == len_comp-1:
                answer = participant[i]
                break


    else:
        answer = list(answer)[0]

    return answer
