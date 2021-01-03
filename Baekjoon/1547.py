M = int(input())

answer = [1]
for n in range(M):
    change = set(map(int,input().split(' ')))
    if answer[0] in change and len(set(change)) == 2:
        answer = list(change - set(answer))

print(answer[0])
