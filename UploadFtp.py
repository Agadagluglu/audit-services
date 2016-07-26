from ftplib import FTP
import time

# les paramètres de connexion au serveur FTP

ftp_host = '172.31.98.159'
ftp_login = 'admin'
ftp_password = 'Azerty1234'


path = '/audits'
ftp = FTP(ftp_host, ftp_login, ftp_password)
print(ftp.getwelcome())
ftp.cwd(path)

f = open('scan.txt', 'rb')
ftp.storbinary("STOR pentest.%s.txt" % time.time(), f)
f.close()

ftp.quit()
ftp.close()
