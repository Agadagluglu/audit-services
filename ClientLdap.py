import socket
import sys


# Menu d'administration
def menu():

    reponse = True
    while reponse:
        print("""
        1. Afficher la base
        2. Ajouter un utilisateur
        3. Supprimer un utilisateur
        4. Authentifier un utilisateur
        5. Quitter
        """)
        reponse = input("Entrez votre choix : ")
        if reponse == "1":
            display()
        elif reponse == "2":
            user = input("Quel est le nom de l'utilisateur à créer ? ")
            adduser(user)
        elif reponse == "3":
            user = input("Quel est le nom de l'utilisateur à supprimer ? ")
            deluser(user)
        elif reponse == "4":
            user = input("Quel est le nom de l'utilisateur ? ")
            password = input("Entrez le mot de passe pour authentifier l'utilisateur : ")
            login(user, password)
        elif reponse == "5":
            print("\n Au revoir.")
            reponse = False
        elif reponse != "":
            print("\n Choix invalide.")

#################################################
#  Mise en place d'un client simple
#  simulation d'une connexion client/serveur
#  """"""""""""""""  version basique """""""""""#

# création d'un socket pour la connexion avec le serveur en local
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connexion au serveur, bloc surveillé, et gestion de l'exception
    sock.connect(('127.0.0.1', 2020))

except socket.error:
    print("la connexion a échoué.......")
    sys.exit()

print(">>> Connexion établie avec le serveur...")
# Envoi et réception de messages
sock.send(b"hello serveur")
msgServer = sock.recv(1024)  # taille par défaut

print(">>> S :", msgServer.decode())

while 1:

    if msgServer == b'FIN' or msgServer == b'':
        break
    else:
        msgClient = input(">>> ")
        msgClient = msgClient.encode()
        print(">>> Envoi vers le serveur")
        sock.send(msgClient)
        msgServer = sock.recv(100)
        print(">>> Reception du serveur")
        print(msgServer.decode())

print(">>> Connexion interrompue par le serveur !!!")
sock.close()
