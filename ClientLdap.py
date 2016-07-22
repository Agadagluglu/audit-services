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
            envoi("display()")
        elif reponse == "2":
            user = input("Quel est le nom de l'utilisateur à créer ? ")
            envoi("adduser(\"" + user + "\")")
        elif reponse == "3":
            user = input("Quel est le nom de l'utilisateur à supprimer ? ")
            envoi("deluser(\"" + user + "\")")
        elif reponse == "4":
            user = input("Quel est le nom de l'utilisateur ? ")
            password = input("Entrez le mot de passe pour authentifier l'utilisateur : ")
            envoi("login(\"" + user + "\" , \"" + password + "\")")
        elif reponse == "5":
            print("\n Au revoir.")
            reponse = False
        elif reponse != "":
            print("\n Choix invalide.")


# Création d'un socket pour la connexion avec le serveur
def envoi(msg_client):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connexion au serveur
        sock.connect(('127.0.0.1', 6666))

    except socket.error:
        print("la connexion a échoué.")
        sys.exit()

    print(">>> Connexion établie avec le serveur.")
    sock.send(str.encode(msg_client))
    msg_server = sock.recv(1024)
    msg_server.decode()
    print(msg_server.decode())

    sock.close()
    return msg_server

menu()
