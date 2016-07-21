# scanneur de port
import socket
import threading
import time
import datetime

hote = '127.0.0.1'
f = open('scan.txt', 'w')

#  pour la date utilise ceci
now = datetime.datetime.now().date()

print("date :", now.strftime('%A %d %B %y'))

#  pour la date et le temps uitlise ceci
now1 = datetime.datetime.now().time()
print(now1)
print("Horaire :", now1.strftime('%H:%M:%S'))
# ('%A %d %y, %H:%M:%S'))


##now = time.time()
##print("date=======", now)

##print ("L'heure et la date actuelle:", time.localtime(now))


f.write("la date : " + str(now) + "\n")
#  ou bien
# f.write(" La date et l'heure :" +now1.strftime('%A %d %y, %H:%M:%S'))
f.write("\n")
f.write('+-----------+---------------+\n')
f.write('|port       |   etat        |\n')
f.write('+-----------+---------------+\n')

for i in range(20, 88):
    try:

        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.connect((hote, i))
        # connexion_principale.listen(5)
        print(" le port est ouvert ", i)
        f.write("le port " + str(i) + "  :ouvert \n")

    except:
        print("le port est fermé", i)
        f.write(" le port " + str(i) + " :fermé \n")

f.close()

f = open('portouvert.txt', 'w')

