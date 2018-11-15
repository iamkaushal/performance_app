s = """+--------------------+
|Agent Version       : 252
|Dlp Family          : I40  Xamaiah(123h)
|System Number       : PasTLan DELL350 Ren10
|SRX Date            : 2.0 07/09/2018
|FIGR   File used    : ArestB.CFG
|Cache Type          : PrzMakeB(12/2)
|Child/Process type  : 13/2
|IServer Addre       : 11.252.112.122
|IServer Version     : 1.50 (22) Sep 02 2018
|Crnt Mmm Mthd       : B9EC Mode
|Date Of LogFile     : wed Sep 20 18:04:43 2018
|Cache Slss          : Sls(4h): Glt:3,Pji:9,Vrs:1,Zbrn:1, 0xEEEE=UnKnown. Zeions Sprtd:4.
|1st ProgramVersion  : Siddd(y) Srs(z) NvnG 5126 loke @ 3.50Bhz
+--------------------+
*ERROR*,System failed
*ERROR*,System.
*ERROR*,Crash
*ERROR*,Powerof
*ERROR*,Poweron
*ERROR*,PowerDown
*ERROR*,PowerReset
*ERROR*,PowerUp
str1Iamdead when
str2Somanytimesgoing when
str3power off power on when
str4127- - - - Im just Going"
str5Bit by bit Going down when?"
str6Iam Dead bcz of parent main

Working..: 53
GoneBit..: 23
Errors..: 6
Warnings: 0"""

import re

log_array = re.split("\s", s)

for i in range(len(log_array)):
    print( str(i) + " " + log_array[i])


agent_version = log_array[10]
dlp_family = log_array[23] + " " + log_array[25]
system_number = log_array[35] + " " + log_array[36] + " " + log_array[37]
srx_date = log_array[52] + " " + log_array[53]
figr_file_used = log_array[63]
cache_type = log_array[76]
child_process_type = log_array[81]
IServer_address = log_array[91]
IServer_version = log_array[99] + " " + log_array[100] + " " + log_array[101] + " " + log_array[102] + " " + log_array[103]
Crnt_mmm_mthd = log_array[114] + " " + log_array[115]
date_of_logfile = log_array[124] + " "  + log_array[125] + " "  + log_array[126] + " "  + log_array[127] + " "  + log_array[128]
cache_slss = log_array[141] + " "  + log_array[142] + " "  + log_array[143] + " "  + log_array[144] + " "  + log_array[145]
first_program_version =  log_array[150] + " " + log_array[151] + " " + log_array[152] + " "  + log_array[153] + " "   + log_array[154] + " "  + log_array[155] + " "  + log_array[156]


warnings = log_array[203]
errors = log_array[201]
GoneBit = log_array[199]
Working = log_array[197]
