import re

with open('Drlll_cfg_D40_11_252_112_121_0_2018-September-19_2148b.err', 'r' ) as f:
# with open('Srlll_cfg_K40_11_252_112_122_0_2018-September-20_2148b.err', 'r' ) as f:
    file_content = f.read()


# ERROR Pattern analyser
error_pattern = re.compile(r'(\*ERROR\*\,)([\w ]+)')
error_matches = error_pattern.findall(file_content)
# subbed_errors = pattern.sub(r'\1', s)

# ERROR PATTERN DEBUGGING CODE
for error in error_matches:
    print(error[0] + error[1])










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



















#
#
#discarded code
#
# log_array = re.split("\s", s)
#
# for i in range(len(log_array)):
#     print( str(i) + " " + log_array[i])
#
#
# agent_version = log_array[4]
# dlp_family = log_array[8] + " " + log_array[9]
# system_number = log_array[13] + " " + log_array[14] + " " + log_array[15]
# srx_date = log_array[19] + " " + log_array[20]
# figr_file_used = log_array[25]
# cache_type = log_array[29]
# child_process_type = log_array[33]
# IServer_address = log_array[37]
# IServer_version = log_array[41] + " " + log_array[42] + " " + log_array[43] + " " + log_array[44] + " " + log_array[45]
# Crnt_mmm_mthd = log_array[50] + " " + log_array[51]
# date_of_logfile = log_array[56] + " "  + log_array[57] + " "  + log_array[58] + " "  + log_array[59] + " "  + log_array[60]
# cache_slss = log_array[64] + " "  + log_array[65] + " "  + log_array[66] + " "  + log_array[67] + " "  + log_array[68]
# first_program_version =  log_array[72] + " " + log_array[73] + " " + log_array[74] + " "  + log_array[75] + " "   + log_array[76] + " "  + log_array[77] + " "  + log_array[78]
#
#
# warnings = log_array[124]
# errors = log_array[122]
# GoneBit = log_array[120]
# Working = log_array[118]
