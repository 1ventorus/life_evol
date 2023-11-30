import os
import time

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

vitesse de simulation : 1 correspond a 1 siècle
"""

# Valeurs d'évolution possibles
uni_cell = "organisme unicellulaire"
plurial_cell = "organisme pluricellulaire"
cell = "cellule"
eye = "système organique des yeux"
human_foot = "pied humain"
human_hand = "main humaine"
monkey_foot = "pied de singe"
griffe = "griffe"
tail = "queue"
wing = "ailes"

# Valeurs d'évolution des organismes
quantity_animals_type = 1
speed = 5

# État des mutations
yes = "oui"
no = "non"
in_take = "en train de se développer"

class WorldSim:
    def __init__(self):
        self.time_step = 1
        self.simulation_duration = 5
        self.repetition_count = speed
        self.is_running = False
        self.population = 2

    def advance_time(self):
        for _ in range(self.repetition_count):
            self.advance_word()
            print("Simulation en cours...")
            self.population *= 2
            self.time_step += 1

        if self.time_step > self.simulation_duration:
            self.stop_simulation()

    def advance_word(self):
        # Simulate the word.advance_time() function
        time.sleep(0.1)

    def stop_simulation(self):
        self.is_running = False

    def reset_simulation(self):
        self.population = 2
        self.is_running = True

    def is_simulation_running(self):
        return self.is_running

def save():
    with open("save.txt", "w+") as fichier:
        fichier.write(f"mutated={WS.mutated}\n")
        fichier.write(f"population={WS.population}\n")

def load():
    with open("save.txt", "r") as fichier:
        for line in fichier:
            key, value = line.strip().split("=")
            if key == "population":
                WS.population = int(value)

def sim():
    WS = WorldSim()
    while True:
        os.system("cls")
        print(BANNER)
        print(HELP)
        print("quantité actuel d'etre vivant ", WS.population)
        print("vitesse de simulation : ", WS.repetition_count)
        print("Exécutez des commandes pour modifier l'avancement du monde.")
        god = input(">>> ")

        if god == "lancer":
            WS.advance_time()

        elif god == "augmenter":
            WS.repetition_count += 1
        elif god == "reduire":
            WS.repetition_count -= 1

        elif god == "save":
            save()

        elif god == "load":
            load()

        elif god == "reset":
            WS.reset_simulation()

        elif god == "close":
            print("au revoir !")
            time.sleep(2)
            os.system("cls")
            break
