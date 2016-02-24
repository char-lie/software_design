WORK_DIR=$(dirname $0)
psql -f ${WORK_DIR}/migrations/drop_dbs.sql -U postgres

