def count_words(book_text):
    count = 0
    book_string_list = book_text.split()
    for word in book_string_list:
        count += 1
    return(count)
