__author__ = 'Nick'

# pre-reqs:
# 1 - download db2 free - https://www14.software.ibm.com/webapp/iwm/web/download.do?source=swg-db2expressc&S_PKG=dlmacosx&S_TACT=100KG31W&lang=en_US&dlmethod=http
# 2 pydb2
# 3 - (mac - odbc administrator http://support.apple.com/kb/dl895)




import ibm_db
#DSN="DRIVER={IBM DB2 CLI DRIVER};DATABASE=%(name)s;HOSTNAME=%(host)s;PORT=%(port)s;PROTOCOL=TCPIP;UID=%(user)s;PWD=%(pass)s;"
dsn="DRIVER={IBM DB2 CLI DRIVER};DATABASE=MCYPRDST;HOSTNAME=32.83.113.246;PORT=60000;PROTOCOL=TCPIP;UID=mcyapp;PWD=dbacce5s;"

#conn = ibm_db.connect(dsn,'','')

#conn = ibm_db.connect("MCYPRDST","mcyapp","")

#import DB2
ibm_db.connect("DATABASE=MCYPRDST;HOSTNAME=32.83.113.246;PORT=60000;PROTOCOL=TCPIP;UID=mcyapp;PWD=;", "", "")

#conn = DB2.connect(dsn='32.83.113.246', uid='mcyapp', pwd='dbacce5s')

#conn.close()


