commands = ['push','pop','size','empty','top']

N = int(input())
arrStack = []


coms = []
for n in range(N):
    coms.append(input().split(' '))



for n in range(N):
    com = coms[n]

    if com[0] == commands[0]: arrStack.append(int(com[1]))

    elif com[0] == commands[1]: 
        if len(arrStack) > 0: print(arrStack.pop())
        else: print(-1)

    elif com[0] == commands[2]: print(len(arrStack))

    elif com[0] == commands[3]:
        if len(arrStack) == 0: print(1)
        else: print(0)

    elif com[0] == commands[4]: 
        if len(arrStack) == 0:
            print(-1)
        else:
            print(arrStack[-1])
