def solution(N,arr1,arr2):
    R = []
    for n in range(N):
        tmp = arr1[n] | arr2[n] 
        tmp = bin(tmp)[2:]
        tmp = '0' * (N-len(tmp)) + tmp
        _tmp = ''
        for m in range(N):
            
            if tmp[m] == '1':
                _tmp += '#'
            else:
                _tmp += ' '
        
        R.append(_tmp)
    return R
