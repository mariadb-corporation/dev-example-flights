#!/bin/bash

host=$1
port=$2
user=$3
pass=$4

# use the arguments to connect to MariaDB SkySQl
mariadb="mariadb --host ${host} --port ${port} --user ${user} -p${pass} --ssl-ca skysql_chain.pem"

# non-SkySQL connection
#mariadb="mariadb --host ${host} --port ${port} --user ${user} -p${pass}"

echo "creating schema..."

# create flights database and airlines, airports, flights tables
${mariadb} < schema/setup.sql

echo "schema created"
echo "loading data..."

# Load airlines into flights.airlines
${mariadb} -e "LOAD DATA LOCAL INFILE 'schema/airlines.csv' INTO TABLE airlines FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'" flights

echo "- airlines.csv loaded into flights.airlines"

# Load airports into flights.airlines
${mariadb} -e "LOAD DATA LOCAL INFILE 'schema/airports.csv' INTO TABLE airports FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'" flights
echo "- airports.csv loaded into flights.airports"

#!/bin/bash
# check for argument, if so use as wildcard for file load match, otherwise load everything
filematch="*"
if [ $# -eq 1 ]
then
  filematch="*$1*"
fi
# load the specified files under the data directory with the file pattern match
for f in data/$filematch.csv; do
  echo "- $f"
  # /usr/bin/cpimport -m2 -s ',' -E '"' columnstore_schema flights -l $f
  ${mariadb} -e "LOAD DATA LOCAL INFILE '"$f"' INTO TABLE flights FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'" flights
done