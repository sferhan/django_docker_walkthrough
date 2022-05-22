#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift


while ! nc -z $host; do
  echo "Waiting for database"
  sleep 1
done

>&2 echo "Postgres is up"

exec "$@"

