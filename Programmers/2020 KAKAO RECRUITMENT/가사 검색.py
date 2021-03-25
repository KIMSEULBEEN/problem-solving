from bisect import bisect_left, bisect_right

def solution(WORD, queries):
    ANSWER = []
    W_sorted, W_sorted_rev = [], []
    for n in range(10001): 
        W_sorted.append([])
        W_sorted_rev.append([])

    # W_sorted에 길이별로 소팅된 리스트 넣기
    for n in range(len(WORD)):
        word = WORD[n]
        W_sorted[len(word)].append(word)
        W_sorted_rev[len(word)].append(word[::-1])

    for n in range(10001): 
        W_sorted[n].sort()
        W_sorted_rev[n].sort()

    def return_min_max_idx(A, min, max):
        i_min = bisect_left(A, min)
        i_max = bisect_right(A, max) - 1
        return i_max - i_min + 1

    for query in queries:
        if query[0] != '?':
            answer = return_min_max_idx(W_sorted[len(query)], query.replace('?','a'), query.replace('?','z'))
        else:
            query = query[::-1]
            answer = return_min_max_idx(W_sorted_rev[len(query)], query.replace('?','a'), query.replace('?','z'))
        ANSWER.append(answer)

    return ANSWER
