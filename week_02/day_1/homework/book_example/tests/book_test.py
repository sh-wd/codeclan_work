import unittest
from src.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Tall, Dark and Hanson", "Alan Hanson", 1878, 100000)


    def test_book_has_title(self):
        self.assertEqual("Tall, Dark and Hanson", self.book.title)


    def test_book_has_author(self):
        self.assertEqual("Alan Hanson", self.book.author)


    def test_book_can_update_title(self):
        self.book.title = "Why I Done What I Did"
        self.assertEqual("Why I Done What I Did", self.book.title)


    def test_book_can_change_author(self):
        self.book.author = "Alan Partridge"
        self.assertEqual("Alan Partridge", self.book.author)
        
    def test_book_can_be_read(self):
        self.assertEqual("It put me into a coma", self.book.read())

    # Add a property of year of publication to book class
    # You will need to update the book instance above to accomodate your new property

    def test_book_has_date_of_publication(self):
        self.assertEqual(1878, self.book.date_of_publication)

    # Add a property of how many books were pulped
    # You will need to update the book instance above to accomodate your new property
    
    def test_book_was_pulped(self):
        self.assertEqual(100000, self.book.number_pulped)
