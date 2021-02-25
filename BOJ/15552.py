import sys

N = int(input())

for n in range(N):
    try:
        input = sys.stdin.readline()
        input = input.rstrip()

        input_split = input.split(' ')

        a = int(input_split[0])
        b = int(input_split[1])
        print(a+b)


    except:
        EOFError
