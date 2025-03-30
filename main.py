def get_books_text(book_text):
    got_book_text = book_text.read()
    return(got_book_text)

from stats import count_words

book_text = None
word_count = 0
with open("books/frankenstein.txt") as text:
    book_text = (get_books_text(text))
    word_count = (count_words(book_text))
    print(f"{word_count} words found in the document")