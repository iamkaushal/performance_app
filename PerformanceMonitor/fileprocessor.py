import os,time
import re
import json
import datetime
from database import DatabaseManagement

class FileProcessor:

    def processFiles(self):
        db = DatabaseManagement()
        for name in os.listdir('./logs'):
            json_str = self.splitFileAndInsert('./logs/'+name)
            db.insertDataToDatabase(json_str)


    def splitFileAndInsert(self,name):
        with open(name) as f:
            file_content = f.read()
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
            temp = re.split('\n', file_content)
            abs_path = os.path.abspath(name)
            now = datetime.datetime.now()
            insertion_date = now.strftime('%Y-%m-%d %H:%M:%S')
            cr_date = time.ctime(os.path.getctime(name))
            creation_date = datetime.datetime.strptime(cr_date, "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d %H:%M:%S")
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

            data = [abs_path,creation_date,insertion_date,agent_version, dlp_family, system_number, srx_date, figr_file_used,
            cache_type, child_process_type, IServer_address, IServer_version, Crnt_mmm_mthd,
            date_of_logfile, cache_slss, first_program_version, errors_json, str_json, working,
            GoneBit, Errors, Warnings,name ]
            print(data)
            return data
