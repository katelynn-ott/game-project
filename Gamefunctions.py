#Gamefunctions.py
#Katelynn Ottmann
#2/18/25

#This program defines purchase item and has three predetermined inputs to test.
#This program also runs a randomized monster generator.
#Documentation and Strings added to the top 
"""
This module contains basic game functions for managing player interactions within the game.
It includes functions for:
- Printing a welcome message
- Displaying a shop menu with prices and items
- Handling purchases
- Generating a random monster with attributes

These functions can be imported into other game modules for use.

Usage Example:
    import gamefunctions

    gamefunctions.print_welcome("PlayerName")
    gamefunctions.print_shop_menu("Sword", 5.99, "Potion", 2.46)
"""


def print_welcome(name: str, width: int = 20):
    """
    Prints a welcome message with the given name always centered to a specific length.

    Parameters:
     name(str): the players name to be displayed with welcome message
        width: the width at which the message with be displayed and centered within.
        
    Returns:
    None
    
    Example:
        print_welcome ("Alice")
        '    Hello, Alice!    '
    """
    message = f"Hello, {name}!"
    print(message.center(width))
    
print_welcome("Katelynn")
print_welcome("Aubrey")
print_welcome("Amanda")


def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """
    Prints a shop menu with two items, aligning item names to the left and prices to the right.

    Parameters:
        Item1 (str): Name of first item
        Item1Price (float): Price of first item
        Item2 (str): Name of second item
        Item2Price (float): Price of second item`````    

    Returns:
        None

    Example:
        print_shop_menu("Sword", 10.99, "Shield", 5.49)
        /----------------------\
        | Sword         $ 10.99 |
        | Shield        $  5.49 |
        \----------------------/
    """
    item1 = f"| {item1Name:<12} ${item1Price:>7.2f} |"
    item2 = f"| {item2Name:<12} ${item2Price:>7.2f} |"
    print("/----------------------\\")
    print(item1)
    print(item2)
    print("\\----------------------/")
print_shop_menu("Orange", .45, "Lemon", .777)
print_shop_menu("Milk", 7.22 , "Fruit Loops", 6.88)



import random
def purchase_item(item_price: float, starting_money: float, quantity_purchase):
    """

    Simulates the purchae of an item based on price, available quanity, money, and desired quantity.
    Reduces the number of items following purchase.

    Parameters:
        item_price (float): Price per item
        starting_money (float): The amount of money player has
        quantity_purchase (int): the number of items player wishes to buy

    Returns:
        tuple: the number of purchased items and remaining money

    Example:
        purchase_item(3.5, 10, 3)
        (3, 0.5)
    """
    total_cost = item_price * quantity_purchase
    if starting_money >= total_cost:
        num_purchased = quantity_purchase
        leftover_money = starting_money - total_cost
    else:
        num_purchased = int(starting_money // item_price)
        leftover_money = starting_money - (num_purchased * item_price)
    return num_purchased, leftover_money

num_purchased, leftover_money = purchase_item(1.23, 10, 3)
print(num_purchased) 
print(leftover_money)  


num_purchased, leftover_money = purchase_item(1.23, 2.01, 3)
print(num_purchased)  
print(leftover_money)  


num_purchased, leftover_money = purchase_item(3.41, 21.12, 2)
print(num_purchased) 
print(leftover_money)  


num_purchased, leftover_money = purchase_item(31.41, 21.12, 1)
print(num_purchased)  
print(leftover_money)  



def get_random_monster():
    monster_type = random.randint(1, 3)

    if monster_type == 1:
        name = "Hydra"
        description = "A five headed serpent that breathes fire out of the middle mouth"
        health_range = (75, 150)
        power_range = (50, 100)
        money_range = (5, 70)
    elif monster_type == 2:
        name = "Fury"
        description = "A winged old woman that carry's a whip and has a long, pointed tail"
        health_range = (60, 100)
        power_range = (5, 95)
        money_range = (100, 150)
    elif monster_type == 3:
        name = "Krakken"
        description = "A sea monster with eight gigantic tentacles, and a mouth that reaks of rotting flesh"
        health_range = (200, 250)
        power_range = (50, 200)
        money_range = (10, 90)
    return name, description, health_range, power_range, money_range

def generate_stats(health_range, power_range, money_range):
    health = random.randint(health_range[0], health_range[1])
    power = random.randint(power_range[0], power_range[1])
    money = random.randint(money_range[0], money_range[1])
    
    return health, power, money
    
def create_random_monster():
    name, description, health_range, power_range, money_range = get_random_monster()
    health, power, money = generate_stats(health_range, power_range, money_range)
    
    return {
        "name": name,
        "description": description,
        "health": health,
        "power": power,
        "money": money
    }

random_monster1 = create_random_monster()

print(f"Name: {random_monster1['name']}")
print(f"Description: {random_monster1['description']}")
print(f"Health: {random_monster1['health']}")
print(f"Power: {random_monster1['power']}")
print(f"Money: {random_monster1['money']}")

random_monster2 = create_random_monster()

print(f"Name: {random_monster2['name']}")
print(f"Description: {random_monster2['description']}")
print(f"Health: {random_monster2['health']}")
print(f"Power: {random_monster2['power']}")
print(f"Money: {random_monster2['money']}")

random_monster3 = create_random_monster()

print(f"Name: {random_monster3['name']}")
print(f"Description: {random_monster3['description']}")
print(f"Health: {random_monster3['health']}")
print(f"Power: {random_monster3['power']}")
print(f"Money: {random_monster3['money']}")

if __name__ == "__main__":
    print_welcome("Katelynn")
    print_welcome("Aubrey", 30)

    print_shop_menu("Sword", 10.99, "Potion", 2.49)

    num_purchased, leftover_money = purchase_item(3.5, 10, 3)
    print(f"Purchased {num_purchased} items. Remaining money: ${leftover_money:.2f}")

    random_monster = create_random_monster()
    print(f"Monster: {random_monster['name']} - {random_monster['description']}")
    print(f"Health: {random_monster['health']}, Power: {random_monster['power']}, Money: {random_monster['money']}")
                     

inventory = ['bow', 'shield']
def add_item(item: str, inventory: list):
    """
    adds an item
    """
    
    inventory.append(item)
    
def remove_item(item: str, inventory: list):
    """
    removes an item
    """

    if item in inventory:
        inventory.remove(item)
def display_inventory(inventory:list):
    """
    Displays the player's inventory.
    """
    print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'}")


shop_items = {
    "Sword": {"price": 10, "type": "weapon", "power": 15},
    "Mystical Amulet": {"price": 25, "type": "special", "effect": "auto-defeat"},
    "Potion": {"price": 5, "type": "consumable", "heal": 20}
}

def buy_item(item_name: str, player_gold: int, inventory: list):
    if item_name in shop_items:
        item = shop_items[item_name]
        if player_gold >= item["price"]:
            inventory.append(item_name)
            return player_gold - item["price"], f"You purchased {item_name}!"
        else:
            return player_gold, "Not enough gold!"
    return player_gold, "Item not found!"

def equip_weapon(inventory: list):
    for item in inventory:
        if item in shop_items and shop_items[item]["type"] == "weapon":
            return item, f"You equipped {item}!"
    return None, "No weapon in inventory!"

def use_special_item(inventory: list):
    if "Mystical Amulet" in inventory:
        inventory.remove("Mystical Amulet")
        return True, "The mystical amulet glows and defeats the monster instantly!"
    return False, "You don't have a special item!"
