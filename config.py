#!/usr/bin/env python

# import
from asyncio import*
import os
import time
import random


# affichage
BANNER = """
  ▄█        ▄█     ▄████████    ▄████████         ▄████████  ▄█    █▄   ▄██████▄   ▄█       
 ███       ███    ███    ███   ███    ███        ███    ███ ███    ███ ███    ███ ███       
 ███       ███▌   ███    █▀    ███    █▀         ███    █▀  ███    ███ ███    ███ ███       
 ███       ███▌  ▄███▄▄▄      ▄███▄▄▄           ▄███▄▄▄     ███    ███ ███    ███ ███       
 ███       ███▌ ▀▀███▀▀▀     ▀▀███▀▀▀          ▀▀███▀▀▀     ███    ███ ███    ███ ███       
 ███       ███    ███          ███    █▄         ███    █▄  ███    ███ ███    ███ ███       
 ███▌    ▄ ███    ███          ███    ███        ███    ███ ███    ███ ███    ███ ███▌    ▄ 
 █████▄▄██ █▀     ███          ██████████        ██████████  ▀██████▀   ▀██████▀  █████▄▄██ 
 ▀                                                                                ▀        
"""

HELP = """
Voici la liste des commandes :
    - lancer : lance 1 siècle de simulation
    - save : sauvegarde votre avancement
    - load : charger une sauvegarde
    - augmenter : augmente le temps passé par tour de simulation (max 10)
    - reduire : déduit le temps passé par tour de simulation (min 1)
    - reset : réinitialise le monde pour recommencer
    - GMode years : modifier l'année de simulation
    - GMode mutate : modifie les mutation aleatoirement

vitesse de simulation : 1 correspond a 1 siècle
"""


uni_cell = "organisme unicellulaire"
plurial_cell = "organisme pluricellulaire"
# valeurs d'évolution possibles

eye = "système organique des yeux"
human_foot = "pied humain"
human_hand = "main humaine"
monkey_foot = "pied de singe"
griffe = "griffe"
tail = "queue"
wing = "ailes"
horn= "corne"
tree_eyes= "trois yeux"

nbr_sim=0

# valeurs d'évolution des organismes
quantity_animals_type = 1
speed = 5

# gestion de la simulation
class WorldSim:
    def __init__(self):
        self.time_step = 1
        self.simulation_duration = 5
        self.repetition_count = speed
        self.is_running = False
        self.population = 2
        self.years= 0
        self.cell=uni_cell

    # lancement de simulation 
    def advance_time(self):
        for _ in range(self.repetition_count):
            self.advance_word()
            print("Simulation en cours...")
            self.cell = plurial_cell

            self.population *=2

            self.time_step += 1        

        if self.time_step > self.simulation_duration:
            if self.population >= 10000000000000:
                self.population -= 1000000000000   

            elif self.population >= 10000000:
                self.population -= 20000

            elif self.population >= 1000:
                self.population -= 100

            elif self.population <= 100:
                pass
            self.years =  self.years+self.repetition_count*100
            self.stop_simulation()

    # fait avancer la simulation dce 1 tour avec un temps de pause
    def advance_word(self):
        time.sleep(0.1)

    # stop la simulation 
    def stop_simulation(self):
        self.is_running = False

    # reset la simulation entière
    def reset_simulation(self):
        self.population = 2
        self.years = 0
        self.is_running = True

    # indique au système que la simulation est en marche
    def is_simulation_running(self):
        return self.is_running

WS = WorldSim()

# mutation
def mutating():
    values = [eye, human_foot, human_hand, monkey_foot, griffe, tail, wing, horn, tree_eyes]
    associations = {}

    for value in values:
        association = random.choice(["oui", "non", "en developpement"])
        associations[value] = association

    print("Mutation actuelle:")
    print("{:<30} {}".format("Mutation", "État"))
    print("-" * 40)
    for key, value in associations.items():
        print("{:<30} {}".format(key, value))
muting = mutating()

# système de sauvegarde
def save(associations, WS):
    with open("save.txt", "w+") as fichier:
        fichier.write(f"mutated={muting}\n")
        fichier.write(f"population={WS.population}\n")
        fichier.write(f"cell={WS.cell}\n")
        fichier.write(f"years={WS.years}\n")

def load():
    with open("save.txt", "r") as fichier:
        for line in fichier:
            key, value = line.strip().split("=")
            if key == "mutated":
                pass
            
            elif key == "population":
                WS.population = int(value)

            elif key == "cell":
                WS.cell = value

            elif key == "years":
                WS.years = int(value)
            

# simulation
def sim():
    associations = {}  
    mutate = 6
    while True:
        os.system("cls")
        print(BANNER)
        print(HELP)
        print("quantité actuel d'être vivant ", WS.population, "k")
        print("vitesse de simulation : ", WS.repetition_count, "siecle par simulation")
        print("être vivant", WS.cell)
        print("vous en êtes à l'année", WS.years)
        mutating()
        print("\nExécutez des commandes pour modifier l'avancement du monde.")
        
        god = input(">>> ")

        # invoque la fonction WS.advance_time()
        if god == "lancer":
            WS.advance_time()

        # augmente le temps écoulé entre chaque simulation
        elif god == "augmenter":
            WS.repetition_count += 1
        # réduis le temps écoulé entre chaque simulation
        elif god == "reduire":
            WS.repetition_count -= 1

        # sauvegarde l'état de la simulation
        elif god == "save":
            save(associations, WS)

        # charge le l'état de la simulation sauvegardé
        elif god == "load":
            load()

        # modifie manuellement l'année a la quelle se trouve la simulation
        elif god == "GMode years":
            print("en quelle année souhaitez-vous être (valeur numérique entière uniquement)?")
            counter = int(input(">>>"))
            WS.years = counter

        # permet de modifier les mution aléatoirement
        elif god == "GMode mutate":
            pass

        # permet de reset l'état de la simulation
        elif god == "reset":
            WS.reset_simulation()

        # permet de fermer le simulateur
        elif god == "close":
            print("au revoir !")
            time.sleep(2)
            os.system("cls")
            break



