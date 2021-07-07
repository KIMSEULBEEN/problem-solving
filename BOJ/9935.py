string_input = input()
string_bomb = input()


len_string_input, len_string_bomb = len(string_input), len(string_bomb)

idx_bomb = 0
string_answer = ""
for _chr in string_input:
    string_answer += _chr
    if len(string_answer) > 0 and string_answer[-1] == string_bomb[idx_bomb]:
        idx_bomb += 1
    else:
        idx_bomb = 0
        if len(string_answer) > 0 and string_answer[-1] == string_bomb[0]:
            idx_bomb += 1

    if idx_bomb == len_string_bomb:
        string_answer = string_answer[:-len_string_bomb]
        idx_bomb = 0
        if len(string_answer) > 0 and string_answer[-1] == string_bomb[0]:
            idx_bomb += 1






if len(string_answer) == 0: string_answer = "FRULA"

print(string_answer)
