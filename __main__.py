import psycopg2


if __name__ == '__main__':
    connection_string = "host='localhost' dbname='db_booking' user='postgres' password='12345'"

    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()

    commands = [
        "BEGIN;",
        "insert into test values (1);",
        "insert into test values (2);",
        "PREPARE TRANSACTION 'mytran';"
    ]

    for c in commands:
        cursor.execute(c)

    cursor.execute("COMMIT PREPARED 'mytran';")

    cursor.close()
    connection.close()

