def solution(num_players, results):

    resultsListWin = [[] for _ in range(num_players + 1)]
    resultsListWin[0].append(-1)

    resultsListLose = [[] for _ in range(num_players + 1)]
    resultsListLose[0].append(-1)
    
    
    for win_player, loss_player in results:
        resultsListWin[win_player].append(loss_player)
        resultsListLose[loss_player].append(win_player)


    for _ in range(num_players):
        for idx_player in range(1, num_players + 1):
            win_players = resultsListWin[idx_player]
            _win_players = []
            for win_player in win_players:
                _win_players.extend(resultsListWin[win_player])
            resultsListWin[idx_player] = list(set(win_players + _win_players))

        for idx_player in range(1, num_players + 1):
            loss_players = resultsListLose[idx_player]
            _loss_players = []
            for loss_player in loss_players:
                _loss_players.extend(resultsListLose[loss_player])
            resultsListLose[idx_player] = list(set(loss_players + _loss_players))


    # print("resultListWin: ", resultsListWin)
    # print("resultListLose: ", resultsListLose)

    answer = 0
    for idx_player in range(num_players + 1):
        if len(resultsListWin[idx_player]) + len(resultsListLose[idx_player]) == num_players - 1:
            answer += 1

    return answer
