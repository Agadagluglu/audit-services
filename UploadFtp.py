# -------------------------------------------------------------#
#        Exemple de script d'acès en FTP à un server           #
#                      vesrion béta                            #
# -------------------------------------------------------------#

from ftplib import FTP

# les paramètres de connexion au serveur FTP

ftp_host = '192.168.1.43'
ftp_login = 'fbouynot'   # configuré sur le serveur avec son pwd
ftp_password = 'Azerty1234'


path = '.'
ftp = FTP(ftp_host, ftp_login, ftp_password)
ftp.debug(7)


print(ftp.getwelcome())
print("Contenu du répertoire courant :")
print(ftp.dir())
print("Changement de répertoire ")
ftp.cwd(path)

print(ftp.mkd("test"))
print("Contenu après changement de répertoire :")
print(ftp.dir())

print("Renommer le fichier test.txt du répertoire en cours :")
ftp.rename('test.txt', 'test_bis.txt')
print("Après avoir renommé le fichier :")
print(ftp.nlst())

print("Renommer le fichier test.txt du répertoire en cours :")
ftp.rename('test_bis.txt', 'test.txt')
print("Après avoir renommé le fichier :")
print(ftp.nlst())

print("Effacement d'un fichier")
ftp.delete('test.txt')
print("Après effacement :")
print(ftp.nlst())

print("Création d'un répertoire :")
ftp.mkd('MYRep')
print("Après création :")
print(ftp.nlst())

print("Effacement du répertoire fichier :")
ftp.rmd('MYRep')
print("Après effacement du répertoire:")
print(ftp.dir())

ftp.quit()
ftp.close()
