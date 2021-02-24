import copy

num_count = int(input())

# 0. 카드 입력 받아들이기
CARD_LIST = []
for n in range(num_count):
    _ = input()
    CARD = input().split(' ')
    CARD_LIST.append(CARD)


ANSWER = []
# CARD_LIST = [['M', 'K', 'U'], ['A', 'S', 'D', 'F', 'G'], ['B', 'A', 'C', 'A', 'B', 'A', 'C']]
for CARD in CARD_LIST:

    if len(CARD) > 1:
        # CARD -> ['M', 'K', 'U']
        STR = [CARD[0]] # ['M']
        # 카드 요소 순서대로

        for n in range(1, len(CARD)):
            _add_str = CARD[n]
            len_STR = len(STR)
            NEW_STR = []
            for m in range(len_STR):
                _str = STR[m] # 'M'
                NEW_STR.append(_str + _add_str)
                NEW_STR.append(_add_str + _str)
            NEW_STR = [sorted(NEW_STR)[0]] # 메모리 에러 추가
            STR = copy.deepcopy(NEW_STR)
        ANSWER.append(sorted(NEW_STR)[0])
    else:
        ANSWER.append(CARD[0])

for answer in ANSWER: print(answer)
