import re

with open('Drlll_cfg_D40_11_252_112_121_0_2018-September-19_2148b.err', 'r' ) as f:
# with open('Srlll_cfg_K40_11_252_112_122_0_2018-September-20_2148b.err', 'r' ) as f:
    file_content = f.read()


# ERROR Pattern analyser
error_pattern = re.compile(r'(\*ERROR\*\,)([\w ]+)')
error_matches = error_pattern.findall(file_content)
# subbed_errors = pattern.sub(r'\1', s)

import json

errors_json = str(json.dumps(error_matches))

# ERROR PATTERN DEBUGGING CODE
# for error in error_matches:
#     print(error[0] + error[1])

# Str pattern analyser
str_pattern = re.compile(r'str\d[\w -?]*')
str_matches = str_pattern.findall(file_content)
str_json = str(json.dumps(str_matches))

working_pattern = re.compile(r'Working..: (\w*)')
working = working_pattern.findall(file_content)[0]
GoneBit = re.findall(r'GoneBit..: (\w*)', file_content)[0]
Errors = re.findall(r'Errors..: (\w*)', file_content)[0]
Warnings = re.findall(r'Warnings: (\w*)', file_content)[0]

# Details analyser

details_pattern = re.compile(r'(:\s)(.*)')

# temp variable to store the details_pattern found in file_content
temp = re.split('\n', file_content)

agent_version           = details_pattern.findall(temp[1])[0][1]
dlp_family              = details_pattern.findall(temp[2])[0][1]
system_number           = details_pattern.findall(temp[3])[0][1]
srx_date                = details_pattern.findall(temp[4])[0][1]
figr_file_used          = details_pattern.findall(temp[5])[0][1]
cache_type              = details_pattern.findall(temp[6])[0][1]
child_process_type      = details_pattern.findall(temp[7])[0][1]
IServer_address         = details_pattern.findall(temp[8])[0][1]
IServer_version         = details_pattern.findall(temp[9])[0][1]
Crnt_mmm_mthd           = details_pattern.findall(temp[10])[0][1]
date_of_logfile         = details_pattern.findall(temp[11])[0][1]
cache_slss              = details_pattern.findall(temp[12])[0][1]
first_program_version   = details_pattern.findall(temp[13])[0][1]


import MySQLdb


db = MySQLdb.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="18061996",     # password
                     db="dbtester")   # name of the database

# Create a Cursor object to execute queries.

# Create a Cursor object to execute queries.
cur = db.cursor()
#

query = 'INSERT into log (id , agent_ver ,dlp_fam ,sys_num ,srx_date , figr_fileused ,cache_type ,child_process_type ,iserver_add ,iserver_ver ,crnt_mmm_mthd ,date_of_logfile ,cache_slss ,first_prog_ver ,errors_json ,str_json ,working ,gonebit ,error ,warning ) VALUES (1, 'agent_version', dlp_family, system_number, srx_date, figr_file_used, cache_type, child_process_type, IServer_address, IServer_version, Crnt_mmm_mthd, date_of_logfile, cache_slss, first_program_version, errors_json, str_json, working, GoneBit, Errors, Warnings );'

# values( "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello");

# query = select * from log;
# Select data from table using SQL query.
cur.execute(query)

db.commit()


# DEBUGGING CODE
# for i in range(1,14):
#     print(i, (details_pattern.findall(temp[i])[0][1]))

# print(agent_version)
# print(dlp_family)
# print(system_number)
# print(srx_date)
# print(figr_file_used)
# print(cache_type)
# print(child_process_type)
# print(IServer_address)
# print(IServer_version)
# print(Crnt_mmm_mthd)
# print(date_of_logfile)
# print(cache_slss)
# print(first_program_version)



# for i in range(1,5):
#     print(details_pattern.findall(temp[i])[0][2])

# errors_list = re.search("(\*ERROR\*\,)([\w ]+)", s)
