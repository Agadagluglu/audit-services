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
            connexion.send(str.encode("L'utilisateur " + user + " existe déjà."))
            file.close()
            return -1
    file.close()
    password = generate_password()
    hashed_password = hashing(password)
    file = open('ldap.bak', 'a')
    file.write(str(user) + ' ' + str(hashed_password) + '\n')
    file.close()
    connexion.send(str.encode("Création de l'utilisateur " + user + " avec le mot de passe " + password))
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
        connexion.send(str.encode("Echec de la suppression : l'utilisateur " + user + " n'existe pas."))
        file.close()
        return -1
    else:
        filewrite = open('ldap.bak', 'w')
        for line in copy_file:
            if line != delline:
                filewrite.write(line)
                print(line)
        filewrite.close()
        connexion.send(str.encode("L'utilisateur " + user + " a été supprimé."))


# Authentification
def login(user, password):

    password = str(hashing(password))
    file = open('ldap.bak', 'r')
    for line in file:
        if user in line:
            (usr, pwd) = line.split()
            if password == pwd:
                file.close()
                connexion.send(str.encode("Connexion de " + user + " réussie"))
                return True
            else:
                file.close()
                connexion.send(str.encode("Tentative échouée de connexion sur le compte " + user))
                return False
    connexion.send(str.encode("Echec de la connexion : le compte " + user + " n'existe pas."))
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
    contenu = file.read()
    connexion.send(contenu.encode())
    file.close()


# Les paramètres du serveur
HOST = '127.0.0.1'     # adresse IP du serveur
PORT = 6666            # port d'écoute du serveur
TAILLE_BUFFER = 1024   # taille max à recevoir, par défaut

# Création d'un socket
Mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET par opposition à AF_UNIX pour socket UNIX

# Liaison du scoket à une adresse IP et un port
Mysocket.bind((HOST, PORT))

# boucle de traitement tant qu'il y a des clients connectés
while 1:
    print(">>> Serveur prêt, en attente d'un client...")

    Mysocket.listen(1)  # écoute d'une connexion

    # Etablissement de la connexion
    connexion, adresse = Mysocket.accept()
    print(">>> Connexion client réussie, adresse IP %s, port %s \n" % (adresse[0], adresse[1]))

    # Réception de message du client
    msgClient = connexion.recv(TAILLE_BUFFER)  # réception de 1024 caractères
    msgServer = msgClient.decode()

    # Execution et renvoi
    exec(msgServer)

Mysocket.close()
