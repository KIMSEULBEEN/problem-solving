import sys

len_items, weight_limit = list(map(int, input().split()))

items = []
weight_min = 9999999
for _ in range(len_items):
    items.append(list(map(int, sys.stdin.readline().rstrip().split())))
    weight_min = items[-1][0] if items[-1][0] < weight_min else weight_min

values_comb = [[0] * (weight_limit + 1) for _ in range(len_items + 1)]  # items * weights



for idx_wei in range(weight_min, weight_limit + 1):
    weight_ref = idx_wei
    weight_total = 0

    for idx_item, (weight_now, value_now) in enumerate(items):
        idx_item += 1

        if weight_now <= weight_ref:
            value_max = value_now if weight_ref - weight_now <= 0 else value_now + values_comb[idx_item - 1][weight_ref - weight_now]
            values_comb[idx_item][idx_wei] = max(value_max, values_comb[idx_item - 1][idx_wei])
        else:
            values_comb[idx_item][idx_wei] = values_comb[idx_item - 1][idx_wei]


# for p in values_comb: print(p)
print(values_comb[-1][-1])