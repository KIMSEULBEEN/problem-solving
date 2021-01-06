import sys

ropes = [0] * 10001

num_ropes = int(sys.stdin.readline())
for _ in range(num_ropes):
    ropes[int(sys.stdin.readline())] += 1

answer = 0
num_ropes_cnt = 0
for w in range(1, 10001):
    if ropes[w] != 0:
        answer_tmp = w * (num_ropes - num_ropes_cnt)
        answer = max(answer_tmp, answer)
        num_ropes_cnt += ropes[w]
        if num_ropes == num_ropes_cnt: break

print(answer)





