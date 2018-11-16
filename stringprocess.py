import re


with open('Srlll_cfg_K40_11_252_112_122_0_2018-September-20_2148b.err', 'r' ) as f:
    s = f.read()


error_pattern = re.compile(r'(\*ERROR\*\,)([\w ]+)')
error_matches = error_pattern.findall(s)
# subbed_errors = pattern.sub(r'\1', s)

for error in error_matches:
    print(error[0] + error[1])



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
