def solution(id_list, report, k):
    id_dict = dict()
    answer = dict()
    for id in id_list:
        id_dict[id] = [0, []]
        answer[id] = 0

    report = list(set(report))
    for rep in report:
        id_report, id_reported = list(rep.split(' '))
        id_dict[id_reported][0] += 1
        id_dict[id_reported][1].append(id_report)


    for id in id_dict.keys():
        k_tmp, id_list_tmp = id_dict[id]
        if k_tmp >= k:
            for id in id_list_tmp:
                answer[id] += 1

    answer = list(answer.values())
    return answer


print(solution(	["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))