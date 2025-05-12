#!/bin/bash
set -e
cmd="$@"

export DATABASE_URL=mysql://$MYSQL_USER:$MYSQL_PASSWORD@mysql:3306/$MYSQL_DATABASE

function db_ready() {
  python <<END
import sys

import MySQLdb
MYSQLHOST="mysql"
try:
    conn = MySQLdb.connect(host=MYSQLHOST, user="$MYSQL_USER", passwd="$MYSQL_PASSWORD", db="$MYSQL_DATABASE")
except MySQLdb.Error:
    sys.exit(-1)
sys.exit(0)
END
}
until db_ready; do
  >&2 printf $"\u274c No Connection to Database \n"
  sleep 1
done

>&2 printf $"\u2714 Database is Up \n"
exec $cmd
