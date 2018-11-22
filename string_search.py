
def search_string(search_ string):
    import MySQLdb
    db = MySQLdb.connect(host="localhost",  # your host
                         user="root",       # username
                         passwd="password",     # password
                         db="dbtester")   # name of the database
    # Create a Cursor object to execute queries.
    cur = db.cursor()
    search_string = 'Agent Version'
    query = "select id, file_path  from log_details where file_content LIKE '%{search_string}%'".format(search_string = search_string)
    cur.execute(query)
    result = cur.fetchall()
    return result
