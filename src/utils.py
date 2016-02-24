import psycopg2
from datetime import datetime, timedelta
from faker import Faker
from os import linesep
import logging


faker = Faker()
USER = 'test_user'
PASSWORD = '123'
HOST = 'localhost'
CONNECTION_PREFIX = "host='{host}' user='{user}' password='{password}'".format(
                     host=HOST, user=USER, password=PASSWORD)


def get_fly_book():
    return {
        'client': faker.name().replace('\'', '\'\''),
        'number': faker.sha1(),
        'fly_from': faker.country_code(),
        'fly_to': faker.country_code(),
        'book_date': str(faker.date_time_this_month())
    }


def get_hotel_book():
    return {
        'client': faker.name().replace('\'', '\'\''),
        'hotel': faker.address().replace('\'', '\'\'').replace('\n', '; '),
        'arrival': str(faker.date_time_this_month()),
        'departure': str(datetime.now() + timedelta(days=faker.random_digit()))
    }


def fly(tm, values):

    query_string = "insert into fly_booking (client_name, fly_number, fly_from, fly_to, book_date) values ('{client}', '{number}', '{fly_from}', '{fly_to}', '{book_date}');"
    queries = [query_string.format(**value) for value in values]

    connection = get_fly_connection()
    cursor = connection.cursor()

    tm.add_transaction(cursor, queries)

    logging.debug('{text}:{newline}{commands}'.format(
                    text='Commands for fly are ready'.upper(),
                    newline=linesep, commands=linesep.join(queries)))

    return connection


def hotel(tm, values):

    query_string = "insert into hotel_booking (client_name, hotel_name, arrival_date, departure_date) values ('{client}', '{hotel}', '{arrival}', '{departure}');"
    queries = [query_string.format(**value) for value in values]

    connection = get_hotel_connection()
    cursor = connection.cursor()

    tm.add_transaction(cursor, queries)

    logging.debug('{text}:{newline}{commands}'.format(
                    text='Commands for hotel are ready'.upper(),
                    newline=linesep, commands=linesep.join(queries)))

    return connection


def get_fly_connection():
    connection_string = "{connection} dbname='{db}'".format(
                          connection=CONNECTION_PREFIX, db='test_db_fly')
    return psycopg2.connect(connection_string)


def get_hotel_connection():
    connection_string = "{connection} dbname='{db}'".format(
                          connection=CONNECTION_PREFIX, db='test_db_hotel')
    return psycopg2.connect(connection_string)


def rollback_prepared(db):
    connection_string = "{connection} dbname='{db}'".format(
                          connection=CONNECTION_PREFIX, db=db)
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("rollback;")
    cursor.execute("select gid from pg_prepared_xacts;")
    for (gid,) in cursor.fetchall():
        cursor.execute("rollback prepared '%s';"%gid)
    connection.close()

