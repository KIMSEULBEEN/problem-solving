def solution(n, t, m, timetable):
    answer = ''
    len_tt = len(timetable)
    
    # Remove ':'
    for x in range(len_tt):
        timetable[x] = int(timetable[x].replace(':',''))
    timetable = sorted(timetable)
    

    # New timetable
    timetable_new = []
    
    # (1) Bus timtable
    timetable_bus = []
    number_bus = [0]*n
    for x in range(n):
        bustime = 900 + int(x*t/60)*100 + (x*t)%60
        timetable_bus.append(bustime)

    # (2) New timetable
    for x in range(len_tt):
        for y in range(n):
            if timetable[x] <= timetable_bus[y] and number_bus[y] < m:
                timetable_new.append(timetable_bus[y])
                number_bus[y] += 1
                break

    # (3) Return arriving time
    if number_bus[n-1] == m:
        tmp = number_bus[n-1] - m + 1
        answer = timetable[len(timetable_new) - tmp] -1

    else:
        answer = timetable_bus[n-1]

    answer = str(answer)

    if len(answer) < 4:
        answer = "0"*(4-len(answer)) + str(answer)
        answer = list(answer)
        if answer[2] == '9':
            answer[2] = '5'

        answer[1] += ':'
        answer = "".join(answer)
    else:
        answer = list(answer)
        if answer[2] == '9':
            answer[2] = '5'
        answer[1] += ':'
        answer = "".join(answer)

    #print(timetable)
    #print(timetable_new)
    #print(number_bus)


    return answer
