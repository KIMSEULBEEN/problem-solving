words = input()
word = input()

answer = 0
while word in words:
    idx_word = words.index(word)
    words = words[:idx_word] + " " + words[idx_word + len(word):]
    answer += 1

print(answer)

