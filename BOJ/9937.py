words = []
len_words = int(input())

chrs = { }
for _ in range(len_words):
    word = input()
    words.append(word)
    len_word = len(word) # 단어 자릿수 파악

    for idx, _chr in enumerate(word):
        digit = 10 ** (len_word - idx - 1)
        # print(word, idx, digit)

        if _chr not in chrs.keys():
            chrs[_chr] = digit
        else:
            chrs[_chr] += digit
chrs = dict(sorted(chrs.items(), key=lambda x: x[1], reverse=True))
numbers = list(range(10 - len(chrs), 10))

# print(numbers)
# print(chrs)

for _chr in chrs.keys():
    chrs[_chr] = numbers.pop()

# print(numbers)
# print(chrs)

answer = 0
for word in words:
    len_word = len(word)
    for idx, _chr in enumerate(word):
        digit = 10 ** (len_word - idx - 1)
        answer += chrs[_chr] * digit

print(answer)