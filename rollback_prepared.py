from src.utils import rollback_prepared


if __name__ == '__main__':
    rollback_prepared('test_db_hotel')
    rollback_prepared('test_db_fly')

