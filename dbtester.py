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
# import json
#
# v = [1, 2, 4]
# s = json.dumps(v)


#
# INSERT into log (agent_ver ,dlp_fam ,sys_num ,srx_date ,
# figr_fileused ,cache_type ,child_process_type ,
# iserver_add ,iserver_ver ,crnt_mmm_mthd ,date_of_logfile ,
# cache_slss ,first_prog_ver ,errors_json ,str_json ,working ,gonebit ,error ,warning )
#
# VALUES (agent_version, dlp_family, system_number, srx_date, figr_file_used, cache_type, child_process_type,
#  IServer_address, IServer_version, Crnt_mmm_mthd, date_of_logfile, cache_slss, first_program_version
# errors_json, str_json, working, GoneBit, Errors, Warnings );


#
# create database `dbtester`;
# CREATE  TABLE `dbtester`.`users` (
#
#   `id` INT NOT NULL ,
#
#   `username` VARCHAR(45) NOT NULL ,
#
#   `password` VARCHAR(45) NULL ,
#
#   `creation_date` DATETIME NULL ,
#
#   PRIMARY KEY (`id`, `username`) );
#
# CREATE  TABLE `dbtester`.`log_details` (
#
#   `id` BIGINT NOT NULL ,
#
#   `file_path` VARCHAR(500) NULL ,
#
#   `creation_date` DATETIME NULL ,
#
#   `insert_date` DATETIME NULL ,
#
#   `agent_version` VARCHAR(100) NULL ,
#
#   `dlp_family` VARCHAR(200) NULL ,
#
#   `system_number` VARCHAR(200) NULL ,
#
#   `srx_date` VARCHAR(200) NULL ,
#
#   `figr` VARCHAR(200) NULL ,
#
#   `cache_type` VARCHAR(200) NULL ,
#
#   `process_type` VARCHAR(100) NULL ,
#
#   `iserver_address` VARCHAR(150) NULL ,
#
#   `iserver_version` VARCHAR(200) NULL ,
#
#   `mmm_method` VARCHAR(150) NULL ,
#
#   `log_date` DATETIME NULL ,
#
#   `cache_slss` VARCHAR(150) NULL ,
#
#   `program_version` VARCHAR(150) NULL ,
#
#   `working` INT NULL ,
#
#   `gone_bit` INT NULL ,
#
#   `errors` INT NULL ,
#
#   `warnings` INT NULL ,
#
#   `file_name` VARCHAR(100) NULL ,
#
#   PRIMARY KEY (`id`) );
#


# create table log (
#   id int NOT NULL AUTO_INCREMENT,
#   PRIMARY KEY (id),
#   agent_ver varchar(128),
#   dlp_fam varchar(128),
#   sys_num varchar(128),
#   srx_date varchar(128),
#   figr_fileused varchar(128),
#   cache_type varchar(128),
#   child_process_type varchar(128),
#   iserver_add varchar(128),
#   iserver_ver varchar(128),
#   crnt_mmm_mthd varchar(128),
#   date_of_logfile varchar(128),
#   cache_slss varchar(256),
#   first_prog_ver varchar(256),
#   errors_json varchar(500),
#   str_json varchar(500),
#   working varchar(10),
#   gonebit varchar(10),
#   error varchar(10),
#   warning varchar(10)
# );
#

#

# CREATE TABLE IF NOT EXISTS examples (
#   id int(11) NOT NULL AUTO_INCREMENT,
#   description varchar(45),
#   PRIMARY KEY (id)
# );


# INSERT INTO examples(description) VALUES ("Hello World");
# INSERT INTO examples(description) VALUES ("MySQL Example");
# INSERT INTO examples(description) VALUES ("Flask Example");
