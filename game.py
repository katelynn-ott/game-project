# game.py
import gamefunctions
import random

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
        else:
            print("Invalid choice. Try again.")
    
    if player_hp <= 0:
        print("You have fallen in battle...")
        print("Game Over")
        exit()
    
    return player_hp, player_gold

print(f"Inventory: {inventory}")

gamefunctions.add_item('spear', inventory)
print("\nAfter adding spear:")
gamefunctions.display_inventory(inventory)

gamefunctions.remove_item('bow', inventory)
print("\nAfter removing bow:")
gamefunctions.display_inventory(inventory)

def main():
    player_hp = 30
    player_gold = 10
    
    while True:
        print("\nYou are in town.")
        print(f"Current HP: {player_hp}, Current Gold: {player_gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Quit")

        while True:
            choice = input("Enter your choice: ")
            if choice in ["1", "2", "3"]:
                break
            print("Invalid input. Please choose 1, 2, or 3.")

        if choice == "1":
            player_hp, player_gold = fight_monster(player_hp, player_gold)
        elif choice == "2":
            if player_gold >= 5:
                player_hp = 30  
                player_gold -= 5
                print("You feel refreshed after a good rest!")
            else:
                print("Not enough gold to sleep!")
        elif choice == "3":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

