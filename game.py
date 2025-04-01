# game.py
import gamefunctions
import random
import json

inventory = []

def save_game(state, filename="savegame.json"):
    """ saves current game """
    required_keys = ["Name", "Inventory", "HP", "Gold"]

    for key in required_keys:
        if key not in state:
            print(f"Warning: Missing key '{key}' in game state. Save may be incomplete.")
    
    with open(filename, "w") as f:
        json.dump(state, f, indent=4)
    print("Game saved successfully.")

def load_game(filename="savegame.json"):
    """Loads the game state from a file."""
    try:
        with open(filename, "r") as f:
            state = json.load(f)
            
        if not all(key in state for key in ["Name", "Inventory", "HP", "Gold"]):
            print("\nSave file is corrupted or missing data. Try starting a new game instead.\n")
            return None
        
        print("Game loaded successfully.")
        return state
    
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return None
    
def fight_monster(player_hp, player_gold):
    
    """
    Handles the combat sequence when the player chooses to fight a monster.

    Parameters:
        player_hp (int): The player's current health points.
        player_gold (int): The player's current amount of gold.

    Returns:
        tuple: Updated player health and gold after the fight.

    The player encounters a random monster and can either:
    - Attack, exchanging damage with the monster.
    - Run away, returning to town with the same stats.
    If the player defeats the monster, they earn gold.
    If the player runs out of HP, the game ends.
    """
    
    monster = gamefunctions.create_random_monster()
    print(f"A wild {monster['name']} appears!")
    print(f"{monster['description']}")
    
    monster_hp = monster['health']
    
    while player_hp > 0 and monster_hp > 0:
        print(f"\nYour HP: {player_hp} | {monster['name']} HP: {monster_hp}")
        print("1) Attack")
        print("2) Run Away")

        action = input("Choose an action: ")
        while action not in ["1", "2"]:
            print("Invalid choice. Please choose 1 or 2.")
            action = input("Choose an action: ")

        if action == "1":
            damage = random.randint(5, 15)  
            monster_damage = random.randint(5, 10)  
            monster_hp -= damage
            player_hp -= monster_damage
            print(f"You deal {damage} damage!")
            print(f"The {monster['name']} hits you for {monster_damage}!")
            
            if monster_hp <= 0:
                print(f"You defeated the {monster['name']}!")
                player_gold += monster['money']
                print(f"You loot {monster['money']} gold!")
                return player_hp, player_gold
        elif action == "2":
            print("You flee back to town!")
            return player_hp, player_gold
    if player_hp <= 0:
        print("You have been slain in battle!")
        print("Game Over")
        exit ()
    
    return player_hp, player_gold


def main():
    print("Hello and welcome to a new adventure!")

    game_state = None

    while game_state is None:
        choice = input("\nDo you want to:\n1) Start a New Game\n2) Load a Saved Game\nEnter choice: ")

        if choice == "1": 
            player_name = input("\nWhat is your name? ")
            gamefunctions.print_welcome(player_name)
        

            while True:
                print(f"Please choose your playstyle, {player_name}:")
                print("1) Knight")
                print("2) Poet")
                print("3) Witch/Warlock")
                print("4) Traveler")
                print("5) Quit")

                class_choice = input("Enter your choice: ")

                if class_choice in ["1", "2", "3", "4", "5"]:
                    break
                print("Invalid input. Please choose 1, 2, 3, 4, or 5.")

            if class_choice == "1":
                player_hp = 200
                player_gold = 45
            elif class_choice == "2":
                player_hp = 130
                player_gold = 55
            elif class_choice == "3":
                player_hp = 180
                player_gold = 40
            elif class_choice == "4":
                player_hp = 120
                player_gold = 100
            elif class_choice == "5":
                print("Thanks for playing!")
                exit()
                
            player_inventory = []  
            game_state = {"Name": player_name, "Inventory": player_inventory, "HP": player_hp, "Gold": player_gold}

            print(f"\nYour HP: {player_hp}\n")
            print(f"Your gold: {player_gold}\n")

            break
        elif choice == "2":  
            game_state = load_game()
            if game_state:
                player_name = game_state["Name"]
                player_inventory = game_state["Inventory"]
                player_hp = game_state["HP"]
                player_gold = game_state["Gold"]

                print(f"\nWelcome back, {player_name}!")
                print(f"Inventory: {player_inventory}")
                print(f"Current HP: {player_hp}, Current Gold: {player_gold}\n")
                break  
            else:
                game_state = None  

        else:
            print("Invalid choice. Please enter 1 or 2.")
        
    while True:
        print("\nYou are in town.")
        print(f"Current HP: {player_hp}, Current Gold: {player_gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Visit the tavern")
        print("4) Visit the blacksmith")
        print("5) Save and Quit")

        while True:
            action = input("Enter your choice: ")
            if action in ["1", "2", "3", "4", "5"]:
                break
            print("Invalid input. Please choose 1, 2, 3, 4, or 5.")

        if action == "1":
            player_hp, player_gold = fight_monster(player_hp, player_gold)
        elif action == "2":
            if player_gold >= 5:
                player_hp = 150  
                player_gold -= 5
                print("You feel refreshed after a good rest!")
            else:
                print("Not enough gold to sleep!")
        elif action == "3":
            print("\nWelcome to the Tavern! Here is what's available:")
            gamefunctions.print_shop_menu("Apple", 0.45, "Milk", 0.777)
            gamefunctions.print_shop_menu("Chicken Leg", 7.22, "Stew", 6.88)

            item_choice = input("Enter the name of the item you want to buy (or 'exit' to leave): ").lower()

            if item_choice == "apple" and player_gold >= 0.45:
                player_inventory.append("Apple")
                player_gold -= 0.45
                print(f"You bought an Apple for 0.45 Gold. Remaining Gold: {player_gold}")
            elif item_choice == "milk" and player_gold >= 0.777:
                player_inventory.append("Milk")
                player_gold -= 0.777
                print(f"You bought Milk for 0.777 Gold. Remaining Gold: {player_gold}")
            elif item_choice == "chicken leg" and player_gold >= 7.22:
                player_inventory.append("Chicken Leg")
                player_gold -= 7.22
                print(f"You bought a Chicken Leg for 7.22 Gold. Remaining Gold: {player_gold}")
            elif item_choice == "stew" and player_gold >= 6.88:
                player_inventory.append("Stew")
                player_gold -= 6.88
                print(f"You bought Stew for 6.88 Gold. Remaining Gold: {player_gold}")
            elif item_choice == "exit":
                print("You leave the shop.")
            else:
                print("Not enough gold or invalid item.")


        
        elif action == "4":
            print("\nWelcome to the shop! Here are the available items:")
            for item, details in gamefunctions.shop_items.items():
                print(f"{item}: {details['price']} Gold")

            item_name = input("Enter the name of the item you want to buy (or 'exit' to leave): ")

            if item_name.lower() == "exit":
                print("You leave the shop.")
            else:
                player_gold, message = gamefunctions.buy_item(item_name, player_gold, inventory)
                print(message)
      

        elif action == "5":
            game_state["Inventory"] = player_inventory
            game_state["HP"] = player_hp
            game_state["Gold"] = player_gold

            print("Saving the following game state:", game_state)
            save_game(game_state)
            print("Game saved. Thanks for playing!")
            break

if __name__ == "__main__":
    main()
