import sys
from collections import deque

# 1. push   2. pop   3. size
# 4. empty  5. front 6. back

# 1. 주어지는 명령의 수
loop = int(sys.stdin.readline().rstrip())

# 2. 명령 수행
QUEUE = deque([])
for n in range(loop):
    # 1) push
    input_str = sys.stdin.readline().rstrip()
    if "pu" == input_str[:2]:
        QUEUE.append(int(input_str[5:]))

    # 2) pop
    elif "po" == input_str[:2]:
        if len(QUEUE) > 0: print(QUEUE.popleft())
        else: print(-1)

    # 3) size
    elif "s" == input_str[0]:
        print(len(QUEUE))

    # 4) empty
    elif "e" == input_str[0]:
        if len(QUEUE) == 0: print(1)
        else: print(0)

    # 5) front
    elif "f" == input_str[0]:
        if len(QUEUE) > 0: print(QUEUE[0])
        else: print(-1)

    # 6) back
    elif "b" == input_str[0]:
        if len(QUEUE) > 0: print(QUEUE[-1])
        else: print(-1)
