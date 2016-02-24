from uuid import uuid4


class TransactionManager:

    def __init__(self):
        self.transactions = []


    def __begin_transaction(self, cursor):
        cursor.execute('BEGIN;')
        return (cursor, uuid4())


    def __prepare_transaction(self, transaction):
        cursor, transaction_id = transaction
        cursor.execute('PREPARE TRANSACTION \'%s\';'%transaction_id)
        print 'Prepared transaction %s'%transaction_id
        self.transactions.append(transaction)


    def __add_queries(self, cursor, queries):
        transaction = self.__begin_transaction(cursor)
        for q in queries:
            cursor.execute(q)
        self.__prepare_transaction(transaction)


    def add_transaction(self, cursor, queries):
        try:
            self.__add_queries(cursor, queries)
        except Exception:
            self.rollback_transactions()
            return False
        return True


    def commit_transactions(self):
        for cursor, transaction_id in self.transactions:
            print 'Commiting %s'%transaction_id
            cursor.execute('COMMIT PREPARED \'%s\';'%transaction_id)


    def rollback_transactions(self):
        for cursor, transaction_id in self.transactions:
            print 'Rolling back %s'%transaction_id
            cursor.execute('ROLLBACK PREPARED \'%s\';'%transaction_id)
        self.transactions = []

