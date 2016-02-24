from random import randint

from src import TransactionManager
from src.utils import get_fly_book, get_hotel_book, \
                      get_fly_connection, get_hotel_connection, fly, hotel


if __name__ == '__main__':

    tm = TransactionManager()

    fly_book = get_fly_book()
    hotel_book = get_hotel_book()
    fly_connection = fly(tm, [fly_book])
    hotel_connection = hotel(tm, [hotel_book])

    tm.commit_transactions()

    fly_connection.close()
    hotel_connection.close()

