from unittest import TestCase, main
from psycopg2 import DataError

from src.TransactionManager import TransactionManager
from src.utils import get_fly_book, get_hotel_book, \
                      get_fly_connection, get_hotel_connection, fly, hotel


class TransactionManagerBase(TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_positive_transaction(self):
        tm = TransactionManager()

        count = 5
        fly_connection = fly(tm, [get_fly_book() for i in xrange(count)])
        hotel_connection = hotel(tm, [get_hotel_book() for i in xrange(count)])

        tm.commit_transactions()

        fly_connection.close()
        hotel_connection.close()


    def test_negative_transaction(self):
        tm = TransactionManager()

        count = 5
        fly_book = get_fly_book()
        hotel_book = get_hotel_book()
        fly_book['book_date'] = 'not a date at all'
        hotel_connection = hotel(tm, [hotel_book])
        with self.assertRaises(DataError):
            fly_connection = fly(tm, [fly_book])

        hotel_connection.close()

