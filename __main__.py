import psycopg2
from random import randint
from os import linesep

from src import TransactionManager


def get_booking_connection():
    connection_string = "host='localhost' dbname='db_booking' user='postgres' password='12345'"
    return psycopg2.connect(connection_string)


def get_hotel_connection():
    connection_string = "host='localhost' dbname='db_hotel' user='postgres' password='12345'"
    return psycopg2.connect(connection_string)


def book(tm, values):

    query_string = "insert into test values (%d);"
    queries = [query_string%v for v in values]

    connection = get_booking_connection()
    cursor = connection.cursor()

    success = tm.add_transaction(cursor, queries)

    if not success:
        return connection

    print 'Commands booking ready'.upper()
    print linesep.join(queries)

    return connection


def hotel(tm, values):

    query_string = "insert into test_hotel values ('%s');"
    queries = [query_string%v for v in values]

    connection = get_hotel_connection()
    cursor = connection.cursor()

    success = tm.add_transaction(cursor, queries)

    if not success:
        print 'Commands for hotel failed'.upper()
        return connection

    print 'Commands for hotel ready'.upper()
    print linesep.join(queries)

    return connection


if __name__ == '__main__':

    tm = TransactionManager()

    booking_connection = book(tm, [randint(0, 1000) for i in range(2)])
    hotel_connection = hotel(tm, ['a', 'b'])

    tm.commit_transactions()

    booking_connection.close()

