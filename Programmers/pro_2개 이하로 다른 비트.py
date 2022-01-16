def solution_idx(number):
    number_str = bin(number)[2:]

    idx_0 = -1
    for num in reversed(number_str):
        if num == "0":
            break
        else:
            idx_0 -= 1

    # 1. idx가 -1일 경우
    if idx_0 == -1:
        return number + 1

    else:
        number_str = '0' + number_str
        number_str_list = list(number_str)
        number_str_list[idx_0] = '1'
        number_str_list[idx_0 + 1] = '0'
        number_str = ''.join(number_str_list)

        return int(number_str, 2)


def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(solution_idx(number))
    return answer

numbers = [1]
print(solution(numbers))