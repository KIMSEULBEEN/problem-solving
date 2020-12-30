repeat = int(input())

for n in range(repeat):

    A,B = input().split()

    A = int(A)
    B = int(B)

    N = B-A


    sum = 1
    num = 0

    distance = 0
    while N>=sum:
        sum += int(num/2) + 1
        num += 1


        distance += 1

    print(distance)

