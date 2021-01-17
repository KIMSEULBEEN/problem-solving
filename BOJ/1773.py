import sys

numStudent, endTime = list(map(int, sys.stdin.readline().split()))
numJoogi = [int(input()) for _ in range(numStudent)]


fireTimes = [0] * (endTime + 1)
answer = 0

if 1 in numJoogi: answer = endTime
else:
    for num in numJoogi:
        n = 1
        fireTime = n*num
        while fireTime <= endTime:
            if fireTimes[fireTime] == 0:
                fireTimes[fireTime] += 1
                answer += 1
            n += 1
            fireTime = n * num

print(answer)
