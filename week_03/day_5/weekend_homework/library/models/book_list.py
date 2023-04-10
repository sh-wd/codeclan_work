from models.book import Book

book_1 = Book('The Lord of the Rings', 'J.R.R. Tolkein', 'Fantasy')
book_2 = Book('Dracula', 'Bram Stoker', 'Horror')
book_3 = Book('The Adventures of Sherlock Holmes', 'Arthur Conan Doyle', 'Crime')
book_4 = Book('Great Expectations', 'Charles Dickens', 'Coming of Age')
book_5 = Book('Jane Eyre', 'Charlotte Bronte', 'Romance')

book_list = [book_1, book_2, book_3, book_4, book_5]

def add_new_book(book):
    book_list.append(book)

def remove_book(book_title):
    book_to_remove = None
    for book in book_list:
        if book.title == book_title:
            book_to_remove = book
            break
    book_list.remove(book_to_remove)
