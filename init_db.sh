WORK_DIR=$(dirname $0)
psql -f ${WORK_DIR}/migrations/create_dbs.sql -U postgres
psql -f ${WORK_DIR}/migrations/migrations_hotel.sql -U postgres -d test_db_hotel
psql -f ${WORK_DIR}/migrations/migrations_fly.sql -U postgres -d test_db_fly

