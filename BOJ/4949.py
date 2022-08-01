"""
BOJ 4949 균형잡힌 세상
"""



while True:
    sentence = input().rstrip()
    if sentence == ".":
        break

    brackets = []
    answer = ""
    for c in sentence:
        if c == "(" or c == "[":
            brackets.append(c)

        elif c == ")" or c == "]":
            if len(brackets) == 0:
                answer = "no"
                break
            else:
                if (brackets[-1] == "(" and c == ")")\
                    or (brackets[-1] == "[" and c == "]"):
                    brackets.pop()
                else:
                    # print(c, brackets, abs(ord(brackets[-1]) - ord(c)))
                    answer = "no"
                    break

    if len(answer) == 0:
        if len(brackets) == 0:
            answer = "yes"
        else:
            answer = "no"
    print(answer)
