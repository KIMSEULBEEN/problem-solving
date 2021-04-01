def solution(dartResult):
    result = 0

    toarr = []
    numarr,jearr,oparr = [],[],['','','']

    
    len_str = len(dartResult)
    idx_past = 0
    for n in range(1,len_str):
        if '0' <= dartResult[n] and dartResult[n] <= '9':
            if '0' <= dartResult[n-1] and dartResult[n-1] <= '9':
                continue
            toarr.append(dartResult[idx_past:n])

            idx_past = n
    toarr.append(dartResult[idx_past:len(dartResult)])

    # print(toarr)

    len_to = len(toarr)

    for n in range(len_to):
        for m in range(len(toarr[n])):
            if '0' > toarr[n][m] or  toarr[n][m] > '9':
                numarr.append(int(toarr[n][0:m]))
                break
        jearr.append(toarr[n][m])

        if len(toarr[n]) == m+2:
            oparr[n] += toarr[n][m+1]

    sumarr = []
    for n in range(len_to):
        # print(numarr)
  
        num = numarr[n]
        if jearr[n] == 'S':
            je = 1
        if jearr[n] == 'D':
            je = 2
        if jearr[n] == 'T':
            je = 3

        sumarr.append(num**je)
        # print(sumarr[0])
        if oparr[n] == '*':
            if len(sumarr) > 1:
                sumarr[len(sumarr)-2] *= 2
            sumarr[len(sumarr)-1] *= 2
            
        if oparr[n] == '#':
            sumarr[len(sumarr)-1] = -sumarr[len(sumarr)-1]
    # print(sumarr)
    

    result = sum(sumarr)
    return result
