#!/usr/bin/env python

import os
import time
import sys
import platform
import subprocess
import urllib.request

BANNER =("""
  ▄█        ▄█     ▄████████    ▄████████         ▄████████  ▄█    █▄   ▄██████▄   ▄█       
 ███       ███    ███    ███   ███    ███        ███    ███ ███    ███ ███    ███ ███       
 ███       ███▌   ███    █▀    ███    █▀         ███    █▀  ███    ███ ███    ███ ███       
 ███       ███▌  ▄███▄▄▄      ▄███▄▄▄           ▄███▄▄▄     ███    ███ ███    ███ ███       
 ███       ███▌ ▀▀███▀▀▀     ▀▀███▀▀▀          ▀▀███▀▀▀     ███    ███ ███    ███ ███       
 ███       ███    ███          ███    █▄         ███    █▄  ███    ███ ███    ███ ███       
 ███▌    ▄ ███    ███          ███    ███        ███    ███ ███    ███ ███    ███ ███▌    ▄ 
 █████▄▄██ █▀     ███          ██████████        ██████████  ▀██████▀   ▀██████▀  █████▄▄██ 
 ▀                                                                                ▀        
  ┌─┐┌─┐┌┬┐┬ ┬┌─┐
  └─┐├┤  │ │ │├─┘
  └─┘└─┘ ┴ └─┘┴  
 """)


def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)


def launch():
    if os.path.exists("config.py"):
        os.remove("config.py")

    if os.path.exists("life_evol_setup.py"):
        os.remove("life_evol_setup.py")
        fetch_file("https://raw.githubusercontent.com/1ventorus/life_evol/main/life_evol_setup.py", "life_evol.py")

    print("lancement de l'installation de life evol")
    fetch_file("https://raw.githubusercontent.com/1ventorus/life_evol/main/config.py", "config.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/life_evol/main/life_evol.py", "life_evol.py")
    print("installation fini,\nvous pouvez maintenant lancer le simulateur")

print(BANNER)
print("bienvenue !")

while True:
    print("lancer l'installation de life evol oui/non")
    execute= input(">>>")

    if execute=="oui":
        launch()
    elif execute=="non":
        print("pour le bon foctionnement du simulateur,\nveuillez le lancer dans l'invite de commande avec :")
        print("python life_evol.py")
        print("en étant dans le fichier où ce trouve le simulateur")
        os.system("cd")
        print("au revoir !")
        break
    else:
        print("je ne comprend pas\nrecommencez")
