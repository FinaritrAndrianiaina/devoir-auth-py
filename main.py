
from getpass import getpass
import auth

username = input("your user name: ")
password = getpass("your password: ")
confirmer = getpass("confirm your password: ")
if password == confirmer:
    auth.save(username, password)
else:
    print("les mdp ne correspondent pas")
print("Test login")
usernameverify = input("your user name: ")
passwordVerify = getpass("your password: ")
if auth.verify(usernameverify,passwordVerify):
    print("Vous êtes connecter")
else:
    print("Erreur pendant la connexion")