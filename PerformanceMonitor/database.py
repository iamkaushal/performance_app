import MySQLdb

db = MySQLdb.connect(host="localhost",user="root", passwd="",db="dbtester")
class DatabaseManagement:
    def authenticate(self,username,password):
        cursor = db.cursor()
        cursor.execute("select username from users where username = %s",[username])
        dbuser = cursor.fetchone()[0]
        if dbuser == username:
            cursor.execute("select password from users where username = %s",[username])
            dbpass = cursor.fetchone()[0]
            if dbpass == password:
                return "True"
            else:
                return "Password Incorrect"
        else:
            return "Username Incorrect."
    
    def insertDataToDatabase(self,data):
        # data = '"''C:\\Users\\Ronit\\Desktop\\ApplicationDashboard\\PerformanceMonitor\\logs\\Drlll_cfg_D40_11_252_112_121_0_2018-September-19_2148b.err',
        #  '2018-11-19 04:50:14', '2018-11-20 09:04:06', '250', 'D40  Xamaiah(123h)', 'PasTLan DELL450 Ren10', 
        #  '2.0 07/21/2018', 'Arest.CFG', 'PrzMake(12/2)', '13/2', '11.252.112.121', '1.50 (21) Sep 02 2018', 
        #  'B9DC Mode', 'Tue Sep 19 18:04:43 2018', 'Sls(4h): Glt:3,Pji:9,Vrs:1,Zbrn:1, 0xEEEE=UnKnown. Zeions Sprtd:4.', 
        #  'Siddd(y) Srs(z) NvnG 5126 loke @ 3.50Bhz', '[["*ERROR*,", "System failed "], ["*ERROR*,", "System"], ["*ERROR*,", "Crash"], 
        #  ["*ERROR*,", "Powerof"], ["*ERROR*,", "Poweron"], ["*ERROR*,", "PowerDown"], ["*ERROR*,", "PowerReset"], ["*ERROR*,", "PowerUp"]]',
        #   '["str1Iamdead when", "str2Somanytimesgoing when", "str3power off power on when", "str4127- - - - Im just Going\\"", "str5Bit by bit Going down when?\\"",
        #    "str6Iam Dead bcz of parent main "]', '58', '21', '6', '0', './logs/Drlll_cfg_D40_11_252_112_121_0_2018-September-19_2148b.err']"
        query = '''INSERT into log_details ( file_path,creation_date,insert_date,agent_version ,dlp_family ,system_number ,srx_date, figr ,
        cache_type ,process_type ,iserver_address ,iserver_version ,mmm_method ,log_date ,
        cache_slss ,program_version ,working ,gone_bit ,errors ,warnings ,file_name )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        cursor = db.cursor()
        cursor.execute(query, data)
        db.commit()
