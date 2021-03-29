from itertools import combinations


def solution(relation):
    answer = 0


    len_ = len(relation[0])
    num = 1

    items = list(range(len_))
    list_comb_m = []
    while(len_ >= num):
        list_comb = list(combinations(items,num))

        
        for comb in list_comb: # (1,2),(1,3),...
            continum = 0
            for comb_m in list_comb_m: # exception
                # print('comb',comb,comb_m)
                if len(set(comb)|set(comb_m)) == len(comb):
                    continum = 1
                    break

            if continum == 1:
                continue

            tmp = []
            for n in range(len(relation)): # row of relation
                tmp_str = ''
                for m in comb: # (1,2)
                    tmp_str += relation[n][m]
                tmp.append(tmp_str)

            if len(tmp) == len(list(set(tmp))): # result check
                answer += 1
                # print(answer,comb)

                list_comb_m.append(comb)
                # print('good')

        num += 1

    return answer
