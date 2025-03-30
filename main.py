def get_books_text(book_text):
    got_book_text = book_text.read()
    return(got_book_text)

def count_words(book_text):
    count = 0
    book_string_list = book_text.split()
    for word in book_string_list:
        count += 1
    return(count)

book_text = None
word_count = 0
with open("books/frankenstein.txt") as text:
    book_text = (get_books_text(text))
    word_count = (count_words(book_text))
    print(f"{word_count} words found in the document")