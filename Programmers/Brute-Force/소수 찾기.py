def solution(numbers):
    from itertools import permutations
    answerSet = set()

    for n in range(1,len(numbers)+1):
        nums = list(permutations(numbers,n))

        for n in nums: 
            num = ''
            for m in n: num += m
            num = int(num)

            if num != 0 and num != 1:
                prime = True
                for n in range(2,num):
                    if num%n == 0:
                        prime = False
                        break
                if prime == True: answerSet.add(num)
    return len(answerSet)
