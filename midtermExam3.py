def make_book(booktitle, book_author, book_length = 100):
    book_dict = {
        'title': booktitle, 
        'author': book_author,
        'length': book_length
    }
    return book_dict 

print(make_book('Ulyess', 'James Joyce', 762))
print(make_book('The Odyessy', 'Homer'))

