import hashlib
import binascii
import random
import string
import socket


# Fonction de hash de password
def hashing(password):
    # user et mot de passe doivent être bind en bytes
    return binascii.hexlify(hashlib.pbkdf2_hmac('sha256', bytes(password, 'UTF-8'), b'Azerty1234', 100000))


# Creation d'utilisateur dans le ldap
def adduser(user):

    file = open('ldap.bak', 'r')
    for line in file:
        if user in line:
            print("L'utilisateur " + user + " existe déjà.")
            file.close()
            return -1
    file.close()
    password = generate_password()
    hashed_password = hashing(password)
    file = open('ldap.bak', 'a')
    file.write(str(user) + ' ' + str(hashed_password) + '\n')
    file.close()
    print("Création de l'utilisateur " + user + " avec le mot de passe " + password)
    return password


# Suppression d'un utilisateur
def deluser(user):

    delline = ""
    file = open('ldap.bak', 'r')
    copy_file = file.readlines()
    file.close()
    for line in copy_file:
        if user in line:
            delline = line
    if delline == "":
        print("Echec de la suppression : l'utilisateur " + user + " n'existe pas.")
        file.close()
        return -1
    else:
        filewrite = open('ldap.bak', 'w')
        for line in copy_file:
            if line != delline:
                filewrite.write(line)
                print(line)
        filewrite.close()
        print("L'utilisateur " + user + " a été supprimé.")


# Authentification
def login(user, password):

    password = str(hashing(password))
    file = open('ldap.bak', 'r')
    for line in file:
        if user in line:
            (usr, pwd) = line.split()
            if password == pwd:
                file.close()
                print("Connexion de " + user + " réussie")
                return True
            else:
                file.close()
                print("Tentative échouée de connexion sur le compte " + user)
                return False
    print("Echec de la connexion : le compte " + user + " n'existe pas.")
    return False


# Génération du mot de passe aléatoire
def generate_password():

    liste_de_char = string.ascii_letters+string.digits
    passwd = ""
    for i in range(12):
        passwd += liste_de_char[random.randint(0, len(liste_de_char)-1)]
    return passwd


def display():
    file = open('ldap.bak', 'r')
    print(file.readlines())
    file.close()

###############################################
# Mise en place d'un serveur simple
# simulation d'une connexion client/serveur
# """""""""""""""""  verson basique """"""""" #

# les paramètres du serveur en local pour le test
HOST = '127.0.0.1'     # adresse IP du serveur
PORT = 1023            # port d'écoute du serveur
TAILLE_BUFFER = 1024   # taille max à recevoir, par défaut

# création d'un socket
Mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # famille et mode

# liaison du scoket à une adresse IP et un port
Mysocket.bind((HOST, PORT))

# boucle de traitement tant qu'il y a des clients connectés
while 1:
    print(">>> Serveur prêt, en attente d'un client...")

    Mysocket.listen(1)  # écoute d'une connexion

# établissement de la connexion
    connexion, adresse = Mysocket.accept()
    print(">>> Connexion client réussie, adresse IP %s, port %s \n" % (adresse[0], adresse[1]))

# dialogue avec le client, envoi de message
    connexion.send(b"hello client")
    print(">>> Vous étes sur les serveur, prêt à recevoir vos msg")
    print(">>> Tapez FIN ou rien si vous souhaitez interrompre la connexion")

# réception de message du client
    msgClient = connexion.recv(TAILLE_BUFFER)  # réception de 1024 caractères
    print('>>> C:', msgClient.decode())

# boucle d'échange avec le client
    while 1:
            if msgClient == b"FIN" or msgClient == b"":
                break

            msgServer = input(">>> ")
            msgServer = msgServer.encode()
            print(">>> Envoi vers le client")
            connexion.send(msgServer)
            msgClient = connexion.recv(TAILLE_BUFFER)
            print(">>> Reception du client")
            print(msgClient.decode())

# fermeture de la connexion
    connexion.send(b"Au revoir")
    print(">>> connexion interompue par le client!!!!")
    connexion.close()
    ch = input("<R>ecommencer <T>erminer?")
    if ch == b'T':
        print('Fin des connexions.')
        break
Mysocket.close()
