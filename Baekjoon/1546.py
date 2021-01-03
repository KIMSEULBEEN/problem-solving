N = input()

parr = input()
parr = parr.split(' ')
parr = list(map(int,parr))
parr = sorted(parr)

lenp = int(len(parr))
maxscore = parr[lenp-1]

for n in range(lenp):
    parr[n] = parr[n]/maxscore
    parr[n] *= 100


print(sum(parr,0)/lenp)
