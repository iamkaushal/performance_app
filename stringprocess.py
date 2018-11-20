import re
import json
import os
import datetime
import time

name = 'Drlll_cfg_D40_11_252_112_121_0_2018-September-19_2148b.err'
# name = 'Srlll_cfg_K40_11_252_112_122_0_2018-September-20_2148b.err'
with open(name, 'r') as f:
    file_content = f.read()
    file_name = name
    error_pattern = re.compile(r'(\*ERROR\*\,)([\w ]+)')
    error_matches = error_pattern.findall(file_content)
    errors_json = str(json.dumps(error_matches))
    str_pattern = re.compile(r'str\d[\w -?]*')
    str_matches = str_pattern.findall(file_content)
    str_json = str(json.dumps(str_matches))
    working_pattern = re.compile(r'Working..: (\w*)')
    working = working_pattern.findall(file_content)[0]
    GoneBit = re.findall(r'GoneBit..: (\w*)', file_content)[0]
    Errors = re.findall(r'Errors..: (\w*)', file_content)[0]
    Warnings = re.findall(r'Warnings: (\w*)', file_content)[0]
    details_pattern = re.compile(r'(:\s)(.*)')
    abs_path = os.path.abspath(name)
    now = datetime.datetime.now()
    insertion_date = now.strftime('%Y-%m-%d %H:%M:%S')
    cr_date = time.ctime(os.path.getctime(name))
    creation_date = datetime.datetime.strptime(cr_date, "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d %H:%M:%S")
    temp = re.split('\n', file_content)
    agent_version           = details_pattern.findall(temp[1])[0][1].rstrip()
    dlp_family              = details_pattern.findall(temp[2])[0][1].rstrip()
    system_number           = details_pattern.findall(temp[3])[0][1].rstrip()
    srx_date                = details_pattern.findall(temp[4])[0][1].rstrip()
    figr_file_used          = details_pattern.findall(temp[5])[0][1].rstrip()
    cache_type              = details_pattern.findall(temp[6])[0][1].rstrip()
    child_process_type      = details_pattern.findall(temp[7])[0][1].rstrip()
    IServer_address         = details_pattern.findall(temp[8])[0][1].rstrip()
    IServer_version         = details_pattern.findall(temp[9])[0][1].rstrip()
    Crnt_mmm_mthd           = details_pattern.findall(temp[10])[0][1].rstrip()
    date_of_logfile         = details_pattern.findall(temp[11])[0][1].rstrip()
    cache_slss              = details_pattern.findall(temp[12])[0][1].rstrip()
    first_program_version   = details_pattern.findall(temp[13])[0][1].rstrip()

    #move file to backup folder after processing
    import shutil
    src = os.path.abspath(name)
    dst = "/home/kaushal/Desktop/performance_app/backup"
    shutil.move(src, dst)

    data = [abs_path, creation_date, insertion_date, file_name, agent_version, dlp_family, system_number, srx_date, figr_file_used, cache_type,  child_process_type, IServer_address, IServer_version, Crnt_mmm_mthd,
    date_of_logfile, cache_slss, first_program_version, errors_json, str_json, working, GoneBit, Errors, Warnings]
    print(data)

import MySQLdb
db = MySQLdb.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="dbtester",     # password
                     db="dbtester")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

file_name = 'testing'
query = '''INSERT into log_details (  file_path, creation_date, insert_date, file_name, agent_ver ,dlp_fam ,sys_num ,srx_date , figr_fileused ,
cache_type ,child_process_type ,iserver_add ,iserver_ver ,crnt_mmm_mthd ,date_of_logfile ,
cache_slss ,first_prog_ver ,errors_json ,str_json ,working ,gonebit ,error ,warning )

VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s)'''

data = [abs_path, creation_date, insertion_date, file_name, agent_version, dlp_family, system_number, srx_date, figr_file_used, cache_type,  child_process_type, IServer_address, IServer_version, Crnt_mmm_mthd,
date_of_logfile, cache_slss, first_program_version, errors_json, str_json, working, GoneBit, Errors, Warnings]

# insert data into table using SQL query.
cur.execute(query, data)
db.commit()
