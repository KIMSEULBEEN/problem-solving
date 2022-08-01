

len_books, len_max = list(map(int, input().split(' ')))
books = list(map(int, input().split(' ')))

books_plus, books_minus = [], []
for book in books:
    if book > 0:
        books_plus.append(book)
    else:
        books_minus.append(book)

books_plus = sorted(books_plus, reverse=True)
books_minus = sorted(books_minus)

number_final = 0
answer = 0

if len(books_plus) > 0 and len(books_minus) > 0:
    if books_plus[0] > bo

while len(books_plus) > 0 or len(books_minus) > 0:
    if len(books_plus) > 0:
        number_final = books_plus[0]
        answer += number_final * 2
        books_plus = books_plus[len_max:]
        print(answer, number_final, books_plus)

    if len(books_minus) > 0:
        number_final = -books_minus[0]
        answer += number_final * 2
        books_minus = books_minus[len_max:]
        print(answer, number_final, books_plus)

answer -= number_final
print(answer)
