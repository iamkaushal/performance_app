#!/usr/bin/python
import MySQLdb


db = MySQLdb.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="18061996",     # password
                     db="dbtester")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

# Select data from table using SQL query.
cur.execute("SELECT * FROM examples")

# print the first and second columns
for row in cur.fetchall() :
    print (row[0], " ", row[1])

#
# CREATE TABLE IF NOT EXISTS examples (
#   id int(11) NOT NULL AUTO_INCREMENT,
#   description varchar(45),
#   PRIMARY KEY (id)
# );


# INSERT INTO examples(description) VALUES ("Hello World");
# INSERT INTO examples(description) VALUES ("MySQL Example");
# INSERT INTO examples(description) VALUES ("Flask Example");
