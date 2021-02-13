num_count = int(input())

INPUT = []
for n in range(num_count):
    INPUT.append(int(input()))

class SUM:
    count = 0

    def sum_123(self,num, k):
        for n in range(1, 4):
            k_tmp = k + n
            if k_tmp < num: self.sum_123(num, k_tmp)
            elif k_tmp == num: self.count += 1


for n in range(len(INPUT)):
    sum = SUM()
    sum.sum_123(INPUT[n], 0)
    print(sum.count)
