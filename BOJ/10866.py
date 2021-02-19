import sys
from collections import deque

# 1) push_front X   2) push_back X   3) pop_front   4) pop_back
# 5) size           6) empty         7) front       8) back

# 1. 주어지는 명령의 수
loop = int(sys.stdin.readline().rstrip())


DEQUE = deque([])
for n in range(loop):
    input_str = sys.stdin.readline().rstrip()

    if input_str[:2] == "pu":
        # 1) push_front X
        if input_str[5] == "f":
            DEQUE.appendleft(int(input_str[10:]))
        # 2) push_back X
        else:
            DEQUE.append(int(input_str[10:]))

    elif input_str[:2] == "po":
        # 3) pop_front
        if input_str[4] == "f":
            if len(DEQUE) > 0: print(DEQUE.popleft())
            else: print(-1)

        # 4) pop_left
        else:
            if len(DEQUE) > 0: print(DEQUE.pop())
            else: print(-1)

    # 5) size
    elif input_str[0] == "s": print(len(DEQUE))

    # 6) empty
    elif input_str[0] == "e":
        if len(DEQUE) == 0: print(1)
        else: print(0)

    # 7) front
    elif input_str[0] == "f":
        if len(DEQUE) > 0: print(DEQUE[0])
        else: print(-1)

    # 8) back
    elif input_str[0] == "b":
        if len(DEQUE) > 0: print(DEQUE[-1])
        else: print(-1)
