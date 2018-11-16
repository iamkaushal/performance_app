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


agent_version = log_array[4]
dlp_family = log_array[8] + " " + log_array[9]
system_number = log_array[13] + " " + log_array[14] + " " + log_array[15]
srx_date = log_array[19] + " " + log_array[20]
figr_file_used = log_array[25]
cache_type = log_array[29]
child_process_type = log_array[33]
IServer_address = log_array[37]
IServer_version = log_array[41] + " " + log_array[42] + " " + log_array[43] + " " + log_array[44] + " " + log_array[45]
Crnt_mmm_mthd = log_array[50] + " " + log_array[51]
date_of_logfile = log_array[56] + " "  + log_array[57] + " "  + log_array[58] + " "  + log_array[59] + " "  + log_array[60]
cache_slss = log_array[64] + " "  + log_array[65] + " "  + log_array[66] + " "  + log_array[67] + " "  + log_array[68]
first_program_version =  log_array[72] + " " + log_array[73] + " " + log_array[74] + " "  + log_array[75] + " "   + log_array[76] + " "  + log_array[77] + " "  + log_array[78]


warnings = log_array[124]
errors = log_array[122]
GoneBit = log_array[120]
Working = log_array[118]
