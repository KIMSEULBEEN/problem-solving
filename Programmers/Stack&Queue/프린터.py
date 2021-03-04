def solution(priorities, location):
    sequences = list(zip(list(range(len(priorities))),priorities))
    locs = []

    while sequences:
        if sequences[0][1] !=  max([seq[1] for seq in sequences]):
            sequences.append(sequences.pop(0))
        else:
            locs.append(sequences.pop(0))

    answer = [loc[0] for loc in locs].index(location) + 1

    return answer
