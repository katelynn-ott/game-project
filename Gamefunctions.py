#Gamefunctions.py
#Katelynn Ottmann
#2/18/25

#This program defines purchase item and has three predetermined inputs to test.
#This program also runs a randomized monster generator.
#Documentation and Strings added to the top 


def print_welcome(name: str, width: int = 20):
    """
    Prints a welcome message with the given name always centered to a specific length.
    Returns:
    None
    """
    message = f"Hello, {name}!"
    print(message.center(width))
    
print_welcome("Katelynn")
print_welcome("Aubrey")
print_welcome("Amanda")


def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """
    Prints a shop menu with two items, aligning item names to the left and prices to the right.
    Returns:
    None
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
