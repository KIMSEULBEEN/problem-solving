n = int(input())
seat = list(map(str,input()))

cnt = 1

for i in seat:
    if i=="S":
        cnt += 1

    if i=="L":
        cnt += 0.5

for n in range(1, 51):
    if seat == ["S"]*n:
        cnt = n
        break

print(int(cnt))
