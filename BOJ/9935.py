string_input = input()
string_bomb = input()


len_string_input, len_string_bomb = len(string_input), len(string_bomb)

idx_bomb, idx_bomb_prev = 0, 0
answer = []
for _chr in string_input:
    answer.append(_chr)
    if _chr == string_bomb[-1] and len(answer) >= len_string_bomb:
        for idx, _chr2 in enumerate(answer[-len_string_bomb:]):
            if _chr2 != string_bomb[idx]:
                break
            if idx == len_string_bomb - 1:
                del answer[-len_string_bomb:]

answer = ''.join(answer)
if len(answer) == 0: answer = "FRULA"
print(answer)
