def solution(S):
    def calculate_len(S, num):
        result = ""
        key, cnt = S[:num], 0
        for n in range(0, len(S), num):
            s = S[n:n + num]
            if s == key:
                cnt += 1
            else:
                if cnt > 1:
                    result += "{}{}".format(cnt, key)
                else:
                    result += "{}".format(key)
                key, cnt = s, 1

        if cnt > 1:
            result += "{}{}".format(cnt, key)
        else:
            result += "{}".format(s)
        return result, len(result)
    length_min = 10000
    for num in range(1, len(S)):
        _, length = calculate_len(S, num)
        if length < length_min: length_min = length
    if len(S) == 1: length_min = 1
    return length_min
