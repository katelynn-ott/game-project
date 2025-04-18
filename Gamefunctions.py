#Gamefunctions.py
#Katelynn Ottmann
#2/18/25
import random

def print_welcome(name: str, width: int = 20):
    message = f"Hello, {name}!"
    print(message.center(width))

def purchase_item(item_price: float, starting_money: float, quantity_purchase):
    total_cost = item_price * quantity_purchase
    if starting_money >= total_cost:
        num_purchased = quantity_purchase
        leftover_money = starting_money - total_cost
    else:
        num_purchased = int(starting_money // item_price)
        leftover_money = starting_money - (num_purchased * item_price)
    return num_purchased, leftover_money  

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
        description = "A winged old woman that carries a whip and has a long, pointed tail"
        health_range = (60, 100)
        power_range = (5, 95)
        money_range = (100, 150)
    elif monster_type == 3:
        name = "Krakken"
        description = "A sea monster with eight gigantic tentacles, and a mouth that reeks of rotting flesh"
        health_range = (200, 250)
        power_range = (50, 200)
        money_range = (10, 90)
    return name, description, health_range, power_range, money_range

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    item1 = f"| {item1Name:<12} ${item1Price:>7.2f} |"
    item2 = f"| {item2Name:<12} ${item2Price:>7.2f} |"
    print("/-----------------------\")  
    print(item1)
    print(item2)
    print("\-----------------------/")

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

def add_item(item: str, inventory: list):
    inventory.append(item)
    
def remove_item(item: str, inventory: list):
    if item in inventory:
        inventory.remove(item)

def display_inventory(inventory:list):
    print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'}")

shop_items = {
    "Sword": {"price": 75, "type": "weapon", "power": 67},
    "Mystical Amulet": {"price": 250, "type": "special", "effect": "auto-defeat"},
    "Potion": {"price": 25, "type": "consumable", "heal": 45}
}

def buy_item(item_name: str, player_gold: int, inventory: list):
    if item_name in shop_items:
        item = shop_items[item_name]
        if player_gold >= item["price"]:
            inventory.append(item_name)
            return player_gold - item["price"], f"You purchased a {item_name}!"
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
