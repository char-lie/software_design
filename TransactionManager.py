class TransactionManager:
    def __init__(self, cursor):
        self.transaction_id = None
        self.cursor = cursor


    def start_transaction(self, transaction_id):
        self.cursor.execute('BEGIN;')
        self.transaction_id = transaction_id

    def prepare_queries(self, queries):
        for q in queries:
            self.cursor.execute(q)

    def prepare_transaction(self):
        self.cursor.execute('PREPARE TRANSACTION \'%s\';'%self.transaction_id)


    def commit_transaction(self):
        self.cursor.execute('COMMIT PREPARED \'%s\';'%self.transaction_id)
        self.transaction_id = None


    def rollback_transaction(self):
        self.cursor.execute('ROLLBACK PREPARED \'%s\';'%self.transaction_id)
        self.transaction_id = None

