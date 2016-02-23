import psycopg2
from random import randint
from os import linesep

from TransactionManager import TransactionManager


if __name__ == '__main__':
    connection_string = "host='localhost' dbname='db_booking' user='postgres' password='12345'"

    query_string = "insert into test values (%d);"
    queries = [query_string%randint(0, 1000) for i in range(2)]

    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()

    tm = TransactionManager(cursor)
    tm.start_transaction('new_transaction')
    tm.prepare_queries(queries)
    tm.prepare_transaction()
    tm.commit_transaction()

    print 'Commands executed'.upper()
    print linesep.join(queries)

    cursor.close()
    connection.close()

