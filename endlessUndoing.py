
# testrun: python3 endlessUndoing.py
# testing upload again

# imports
import time
import random
import os
import sys
import json #for saving game
import colorama
from colorama import init, Fore,  Back, Style
init(autoreset=True)
import shutil
columns = shutil.get_terminal_size().columns

# terminal config
def set_terminal_title(title):
    sys.stdout.write(f"\x1b]2;{title}\x07")
    sys.stdout.flush()
set_terminal_title("an endless undoing")

# clear terminal
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# title
def title_screen():
    time.sleep(2)
    print(Back.WHITE + Fore.BLACK + "                    ".center(columns))
    time.sleep(.1)
    print(Back.WHITE + Fore.BLACK + "                    ".center(columns))
    time.sleep(.1)
    print(Back.WHITE + Fore.BLACK + " an endless undoing ".center(columns))
    time.sleep(.1)
    print(Back.WHITE + Fore.BLACK + "                    ".center(columns))
    time.sleep(.1)
    print(Back.WHITE + Fore.BLACK + "                    ".center(columns))
    time.sleep(2)
    print()

# rolls
def roll_d20():
    return random.randint(1, 20)

def roll_d10():
    return random.randint(1,10)

def roll_d6():
    return random.randint(1, 6)

# narrator config
def type_text_sys(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# player config
class Player:
    def __init__(self, name, plClass=None):
        self.name = name
        self.hp = 0 
        self.mp = 0
        self.attack = 0
        self.defense = 0
        self.skilltree = ""
        self.startingability = ""
        self.level = 0
        self.xp = 0
        self.xp_to_next_level = 100
        self.location = None
        self.inventory = []

# classes config
class wanderer(Player):
    def __init__(self, name):
        super().__init__(name)

        self.base_hp = 4
        self.base_mp = 2
        self.base_atk = 3
        self.base_def = 5

        self.hp_roll = roll_d10()
        self.mp_roll = roll_d6()
        self.atk_roll = roll_d6()
        self.def_roll = roll_d10()
    
        self.hp = 4 + self.hp_roll
        self.mp = 2 + self.mp_roll
        self.attack = 3 + self.atk_roll
        self.defense = 5 + self.def_roll

        self.skilltree = "knowledge"
        self.startingability = "outwit"

class mystic(Player):
    def __init__(self, name):
        super().__init__(name)

        self.base_hp = 3
        self.base_mp = 4
        self.base_atk = 2
        self.base_def = 5

        self.hp_roll = roll_d6()
        self.mp_roll = roll_d10()
        self.atk_roll = roll_d6()
        self.def_roll = roll_d10()

        self.hp = 3 + self.hp_roll
        self.mp = 4 + self.mp_roll
        self.attack = 2 + self.atk_roll
        self.defense = 5 + self.def_roll
        self.skilltree = ""
        self.startingability = ""

class degenerate(Player):
    def __init__(self, name):
        super().__init__(name)

        self.base_hp = 2
        self.base_mp = 3
        self.base_atk = 5
        self.base_def= 4

        self.hp_roll = roll_d6()
        self.mp_roll = roll_d6()
        self.atk_roll = roll_d10()
        self.def_roll = roll_d10()

        self.hp = 2 + self.hp_roll
        self.mp = 3 + self.mp_roll
        self.attack = 5 + self.atk_roll
        self.defense = 4 + self.def_roll
        self.skilltree = ""
        self.startingability = ""

class sorcerer(Player):
    def __init__(self, name):
        super().__init__(name)

        self.base_hp = 3
        self.base_mp = 5
        self.base_atk = 2
        self.base_def= 4

        self.hp_roll = roll_d6()
        self.mp_roll = roll_d10()
        self.atk_roll = roll_d10()
        self.def_roll = roll_d6()

        self.hp = 3 + self.hp_roll
        self.mp = 5 + self.mp_roll
        self.attack = 2 + self.atk_roll
        self.defense = 4 + self.def_roll
        self.skilltree = ""
        self.startingability = ""

# game prologue
def game_prologue():
    type_text_sys("...hello.")
    time.sleep(2)
    type_text_sys("apologies, but you aren't able to do much at the moment...")
    time.sleep(2)
    type_text_sys("you see... you don't exist yet. ")
    time.sleep(2)
    type_text_sys("care to change that? (yes/no): ")
    print()

    while True:
        choice = input(Fore.LIGHTYELLOW_EX).lower()
        if choice in ("yes", "no"):
            break
        print()
        type_text_sys("...see, i told you you can't do much... yet.")
        time.sleep(2)
        type_text_sys("now, make your first choice correctly: ")
        continue

    if choice == "no":
        print()
        type_text_sys("mmm. probably for the best.")
        time.sleep(2)
        type_text_sys("goodbye.")
        time.sleep(2)
        sys.exit()
    if choice == "yes":
        print()
        type_text_sys("wonderful... i hope you don't regret it.")
        time.sleep(2)

# character creation
def character_creation():
    print()
    print(Fore.GREEN + "creation:")
    print             ("---------")
    type_text_sys("what is your name? ")
    print()
    plName = input(Fore.LIGHTYELLOW_EX)
    print()
    type_text_sys(f"so be it. you are {plName}.")
    time.sleep(1)
    type_text_sys("and are you...")
    time.sleep(.1)
    print(f"a {Fore.MAGENTA}wanderer{Style.RESET_ALL}, a {Fore.LIGHTCYAN_EX}mystic{Style.RESET_ALL}, a {Fore.RED}degenerate{Style.RESET_ALL}, or a {Fore.BLUE}sorcerer{Style.RESET_ALL}? (or type {Fore.YELLOW}info{Style.RESET_ALL})")
    print()

# assign class
    while True:
        choice = input(Fore.LIGHTYELLOW_EX).lower()
        print()

        if choice == "wanderer":
            player = wanderer(plName)
            print(f"welcome to this world, {Fore.YELLOW + plName + Style.RESET_ALL} the {Fore.MAGENTA}wanderer{Style.RESET_ALL}.")
            print()
            break

        if choice == "mystic":
            player = mystic(plName)
            print(f"welcome to this world, {Fore.YELLOW + plName + Style.RESET_ALL} the {Fore.LIGHTCYAN_EX}mystic{Style.RESET_ALL}.")
            print()
            break

        if choice == "degenerate": 
            player = degenerate(plName)
            print(f"welcome to this world, {Fore.YELLOW + plName + Style.RESET_ALL} the {Fore.RED}degenerate{Style.RESET_ALL}")
            print()
            break

        if choice == "sorcerer":
            player = sorcerer(plName)
            print(f"welcome to this world, {Fore.YELLOW + plName + Style.RESET_ALL} the {Fore.BLUE}sorcerer{Style.RESET_ALL}:")
            print()
            break

        elif choice == "info":
            print()
            print(Fore.GREEN + "class descriptions:")
            print             ("-------------------")
            time.sleep(.1)
            print(f"the {Fore.MAGENTA}wanderer{Style.RESET_ALL} is well-travelled, learned, and resiliant. they prefer to reason over physical confrontation.")
            print()
            time.sleep(.1)
            print(f"the {Fore.LIGHTCYAN_EX}mystic{Style.RESET_ALL} is measuered and wise. they do not approve of conflict but they have access to great inner power.")
            print()
            time.sleep(.1)
            print(f"the {Fore.RED}degenerate{Style.RESET_ALL} is a lowly thug with little to lose. they are brutally opportunistic, tenacious, and love a fight.")
            print()
            time.sleep(.1)
            print(f"the {Fore.BLUE}sorcerer{Style.RESET_ALL} is mysterious and shrewd. they are committed to their studies of magic and eager to develop their skills.")
            print()
            time.sleep(.1)
            print()
            print(Fore.GREEN + "base stats and modifiers:")
            print             ("-------------------------")
            time.sleep(.1)
            print(f"{Fore.MAGENTA}wanderer{Style.RESET_ALL}:    |HP: 4 +d10| * |MP: 2  +d6| * |ATK: 3  +d6| * |DEF: 5 +d10| * |SKILL-TREE: knowledge|")
            print()
            time.sleep(.1)
            print(f"{Fore.LIGHTCYAN_EX}mystic{Style.RESET_ALL}:      |HP: 3  +d6| * |MP: 4 +d10| * |ATK: 2  +d6| * |DEF: 5 +d10| * |SKILL-TREE: mysticism|")
            print() 
            time.sleep(.1)
            print(f"{Fore.RED}degenerate{Style.RESET_ALL}:  |HP: 2  +d6| * |MP: 3  +d6| * |ATK: 5 +d10| * |DEF: 4 +d10| * |SKILL-TREE: brutality|")
            print()
            time.sleep(.1)
            print(f"{Fore.BLUE}sorcerer{Style.RESET_ALL}:    |HP: 3  +d6| * |MP: 5 +d10| * |ATK: 2 +d10| * |DEF: 4  +d6| * |SKILL-TREE: conjuring|")
            print()
            print("type your chosen class name: ")
            print()

        else:
            print("please type a valid class name: ")
         
# roll and display
    time.sleep(2)
    type_text_sys("now let's see how chance treats you: ")
    time.sleep(2)
    print(f"press {Fore.YELLOW}enter{Style.RESET_ALL} to roll for hp")
    input(Fore.LIGHTYELLOW_EX).lower()
    time.sleep(2)
    print(f"you roll a {player.hp_roll}, plus base {player.base_hp} for total HP: {player.hp}")
    print()
    time.sleep(1)
    print(f"press {Fore.YELLOW}enter{Style.RESET_ALL} to roll for mp")
    input(Fore.LIGHTYELLOW_EX).lower()
    time.sleep(2)
    print(f"you roll a {player.mp_roll}, plus base {player.base_mp} for total MP: {player.mp}")
    print()
    time.sleep(1)
    print(f"press {Fore.YELLOW}enter{Style.RESET_ALL} to roll for attack")
    input(Fore.LIGHTYELLOW_EX).lower()
    time.sleep(2)
    print(f"you roll a {player.atk_roll}, plus base {player.base_atk} for total ATTACK: {player.attack}")
    print()
    time.sleep(1)
    print(f"press {Fore.YELLOW}enter{Style.RESET_ALL} to roll for defense")
    input(Fore.LIGHTYELLOW_EX).lower()
    time.sleep(2)
    print(f"you roll a {player.def_roll}, plus base {player.base_def} for total DEFENSE: {player.defense}")
    print()
    time.sleep(1)
    print(f"entering world...")
    time.sleep(5)

# ^^^^^^^^^^^^^^^^
# player mechanics

# area blueprint
class Area: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.actions = []
    
    def connect(self, direction, area):
        self.exits[direction] = area

# areas
# 1. starting zone 
path = Area(
    "location: path to town",
    "a narrow path through a sparse, rotting forest. up ahead, a small town you've never been to."
)

town_gate = Area(
    "town gate",
    "the town is enclosed within an unimpressive wooden wall, the main door guarded by a modestly equipped guard."
)

town_center = Area(
    "town center",
    "a quiet town center decorated by a large tree. small streets splinter off in every direction between various buildings. nothing looks very new or nice."
)

path.connect("south", town_gate)
town_gate.connect("north", path)

town_gate.connect("south", town_center)
town_center.connect("north", town_gate)

# ^^^^^^^^^^^^^^^
# world mechanics

# setup
# vvvvv

clear_terminal()
title_screen()
game_prologue()
character_creation()

# user experience
# vvvvvvvvvvvvvvv

Player.location = path 

while True:
    Area = Player.location
    print(f"\n{Area.name}")
    print(Area.description)

    if Area.exits:
        print("exits:", ", ".join(Area.exits.keys()))

    command = input("> ").lower().strip()

    if command in ("quit", "exit"):
        print("you exit life.")
        break

    elif command in Area.exits:
        Player.location = Area.exits[command]
    else:
        print("invalid command.")
        