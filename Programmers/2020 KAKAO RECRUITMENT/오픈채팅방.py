def idmatching(records):
    len_re = len(records)

    ID_name = {}

    for record in records:
        r = record.split()
        if r[0][0] == 'E':
            ID_name[r[1]] = r[2]

        elif r[0][0] == 'C':
            ID_name[r[1]] = r[2]

    return ID_name


def solution(records):
    answer = []
    ID_name = idmatching(records)

    for record in records:
        r = record.split()
        if r[0][0] == 'E':
            answer.append(ID_name[r[1]] + "님이 들어왔습니다.")

        elif r[0][0] == 'L':
            answer.append(ID_name[r[1]] + "님이 나갔습니다.")

    
    return answer
