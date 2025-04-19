# Katelynn Ottmann
# gamefunctions.py
# 04/18/25

"""gamefunctions.py

Contains utility functions for the Python adventure game:
- save/load game state
- print welcome message
- handle shop interactions
- generate and fight monsters
"""
import json
import random
from wanderingMonster import WanderingMonster

def print_welcome(name, width):
    print("-" * (width * 2))
    print(f"Welcome, {name}, to the Adventure Game!".center(width * 2))
    print("-" * (width * 2))

def shop(gold):
    print("\n" + "-" * 30)
    print(f"Welcome to the shop! (Gold: {gold})")
    print("1. Buy sword - 10 gold")
    print("2. Buy potion - 5 gold")
    print("3. Exit shop")
    print("-" * 30)
    while True:
        choice = input("Choose an item: ")
        if choice == "1":
            if gold >= 10:
                gold -= 10
                print("You bought a sword.")
            else:
                print("Not enough gold.")
        elif choice == "2":
            if gold >= 5:
                gold -= 5
                print("You bought a potion.")
            else:
                print("Not enough gold.")
        elif choice == "3":
            print("Leaving the shop.")
            break
        else:
            print("Invalid choice.")
    return gold

def sleep(hp, gold):
    print("\nYou rest at the inn.")
    if gold >= 5:
        gold -= 5
        hp = 30
        print("You feel refreshed. HP fully restored.")
    else:
        print("Not enough gold to rest.")
    return hp, gold

def equip_weapon():
    print("You equipped your weapon. (Feature placeholder)")

def fight_monster(monster):
    while monster.hp > 0:
        action = input("Do you want to [f]ight or [r]un? ").strip().lower()
        if action == "f":
            hit = random.randint(1, 10)
            print(f"You hit the {monster.name} for {hit} damage!")
            monster.hp -= hit
            if monster.hp <= 0:
                print(f"You have defeated the {monster.name}!")
                return "win"
            
            monster_hit = random.randint(1, 10)
            print(f"The {monster.name} attacks you for {monster_hit} damage!")
           
        elif action == "r":
            print("You run away from the battle!")
            return "run"
        else:
            print("Invalid input.")
    return "win"

def save_game(player_pos, player_hp, player_gold, monsters):
    data = {
        "player_pos": player_pos,
        "player_hp": player_hp,
        "player_gold": player_gold,
        "monsters": [m.to_dict() for m in monsters]
    }
    with open("savefile.json", "w") as f:
        json.dump(data, f)
    print("Game saved.")

def load_game():
    try:
        with open("savefile.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def new_random_monster():
    name = random.choice(["Sprite", "Slime", "Ghost"])
    position = (random.randint(0, 9), random.randint(0, 9)) 
    if name == "Sprite":
        color = (255, 0, 0)
        hp = 10
    elif name == "Slime":
        color = (0, 255, 0)
        hp = 15
    else:
        color = (255, 255, 0)
        hp = 20
    gold = random.randint(5, 15)
    return WanderingMonster(position, color, gold, name, hp)



def generate_monsters():
    return [new_random_monster() for _ in range(2)]


def test_functions():

    print_welcome("Kate", 20)
    print_welcome("Audrey", 30)
    print_welcome("Alex", 25)

    print_shop_menu("Apple", 31, "Pear", 1.234)
    print_shop_menu("Egg", 0.23, "Bag of Oats", 12.34)
    print_shop_menu("Milk", 2.5, "Cookies", 3.99)

    print(purchase_item(1.23, 10, 3))
    print(purchase_item(1.23, 2.01, 3))
    print(purchase_item(3.41, 21.12))
    print(purchase_item(31.41, 21.12))

    for _ in range(3):
        m = new_random_monster()
        print(m)


if __name__ == "__main__":
    test_functions()
