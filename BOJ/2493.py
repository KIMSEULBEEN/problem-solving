len_towers = int(input())
towers = list(map(int, input().split(' ')))
answers, tower_stack = [], []

for idx, tower in enumerate(towers):
    if len(tower_stack) == 0:
        answers.append(0)
        tower_stack = [[idx, tower]]

    else:
        if tower >= tower_stack[0][1]: # 스택 중 최댓값보다 클 경우
            answers.append(0)
            tower_stack = [[idx, tower]]

        else:
            tower_tmp = tower_stack[-1][1]
            while tower_tmp < tower:
                tower_stack.pop()
                tower_tmp = tower_stack[-1][1]

            answers.append(tower_stack[-1][0] + 1)
            tower_stack.append([idx, tower])

print(*answers)
