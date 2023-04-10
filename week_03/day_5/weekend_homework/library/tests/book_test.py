import unittest
from models.book import Book
from models.book_list import *

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book_1 = Book('Frankenstein', 'Mary Shelley', 'Horror')
        self.book_2 = Book('The Time Machine', 'H. G. Wells', 'Science Fiction')

        self.book_list = [self.book_1, self.book_2]

    def test_book_has_title(self):
        self.assertEqual("Frankenstein", self.book_1.title)

    def test_book_has_author(self):
        self.assertEqual("Mary Shelley", self.book_1.author)

    def test_book_has_genre(self):
        self.assertEqual("Horror", self.book_1.genre)

    def test_add_book_to_library(self):
        book_3 = Book('Moby Dick', 'Herman Melville', 'Adventure')
        add_new_book(book_3)
        self.assertEqual(3, len(self.book_list))