string_input = input()
string_bomb = input()

len_string_input, len_string_bomb = len(string_input), len(string_bomb)

idx_bomb, idx_bomb_prev = 0, 0
answer = []
for _chr in string_input:
    answer.append(_chr)
    if _chr == string_bomb[-1]:
        if ''.join(string_bomb[-len_string_bomb:]) == string_bomb:
            del answer[-len_string_bomb:]

answer = ''.join(answer)
if len(answer) == 0: answer = "FRULA"
print(answer)
