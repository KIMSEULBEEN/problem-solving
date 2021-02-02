idx = int(input())
piboList, n = [0,1], 0

while len(piboList) <= idx:
    piboList.append(piboList[n] + piboList[n+1])
    n += 1

print(piboList[idx])
