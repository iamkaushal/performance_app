import MySQLdb

def radiobutton(column):

    db = MySQLdb.connect(host="localhost",  # your host
                         user="root",       # username
                         passwd="dbtester",     # password
                         db="dbtester")   # name of the database

    cur = db.cursor()
    query = 'SELECT {column} from log_details'.format(column = column)
    cur.execute(query)
    result = cur.fetchall()
    return result
