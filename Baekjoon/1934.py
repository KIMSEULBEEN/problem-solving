NUM = int(input())


answer = []
for n in range(NUM):
    nums = sorted(list(map(int,input().split(' '))))

    divNo = 0
    for m in range(1,int((nums[0]+2)/2)):
        if nums[0] % m == 0 and nums[1] % m == 0:
            divNo = m

    if nums[1] % nums[0] == 0:
        divNo = nums[0]


    answer.append(int(nums[0]*nums[1]/divNo))


for num in answer:
    print(num)


