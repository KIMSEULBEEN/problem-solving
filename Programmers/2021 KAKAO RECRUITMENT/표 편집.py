"""
프로그래머스 2021 카카오 채용연계형 인턴십
표 편집

"""


def solution(n, k, cmd):
    """
    :param n: 표의 행 길이
    :param k: 시작 index
    :param cmd: 수행 명령들
    :return: [0, n-1] 행 범위에 해당하는 O,X 값 (str)


    "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
    "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
    "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
    "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
    """
    results = ['O'] * n
    idx = k

    idx_removed = []

    for c in cmd:
        c_type = c[0]

        # "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
        if c_type == 'U':
            move_all = int(c[2])
            move = 0
            while move < move_all:
                idx -= 1
                if results[idx] == 'O':
                    move += 1

        # "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
        elif c_type == 'D':
            move_all = int(c[2])
            move = 0
            while move < move_all:
                idx += 1
                if results[idx] == 'O':
                    move += 1

        # "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
        elif c_type == 'C':
            idx_removed.append(idx)
            results[idx] = 'X'

            idx_start = idx

            # 바로 아랫 항
            idx_down = idx_start
            move = 0
            while move < 1 and idx_down < n - 1:
                idx_down += 1
                if results[idx_down] == 'O':
                    move += 1

            # 바로 윗 항 (가장 마지막 행일 경우 선택)
            idx_up = idx_start
            move = 0
            while move < 1 and idx_up > 0:
                # print("good")
                idx_up -= 1
                if results[idx_up] == 'O':
                    # print("good2")
                    move += 1

            # 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
            if idx_down == n - 1 and results[idx_down] == 'X':
                idx = idx_up
                # print('good')
            else:
                idx = idx_down
            # print(idx)

        # "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
        elif c_type == 'Z':
            results[idx_removed.pop()] = 'O'

    result = ''.join(results)
    return result

"""
8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
"OOOOXOOO"

8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
"OOXOXOOO"

8, 7, ["C", "C"]
OOOOOOXX
"""

n, k, cmd = 8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n, k, cmd))