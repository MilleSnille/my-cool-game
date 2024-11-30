import classes 
import random as rand
import inventory

door_alternatives = ["Trap", "Monster", "Chest" ] 
# chosen_alternative = random.choice(door_alternatives) 


def get_random_enemy(): 
    global random_enemy
    enemy_types = [
        classes.enemy("ZOMBIE", 100, 5),
        classes.enemy("SCOBBY DOO", 55, 20),
        classes.enemy("DIDDY", 150, 10),
        classes.enemy("Terminator", 200, 15)
    ]

    random_enemy = rand.choice(enemy_types)
    return random_enemy
    

def enemy_encounter(): 
    global random_enemy
    print(f"You encounter {get_random_enemy()}")

def get_random_chest_item():
    global random_item
    chest_items = [
        classes.item("Wood Sword", 15, 0),
        classes.item("Acid bottle", 20, 0),
        classes.item("Mop", 10, 0),
        classes.item("Glass Shard", 15, 0),
        classes.item("Energy Sword", 30, 0),
        classes.item("Fire Flower", 25, 0),
        classes.item("Estus Flask", 0, 100)
    ]

    random_item = rand.choice(chest_items)
    return random_item

def add_random_item(): 
    global random_item
    if len(inventory.inv) >= 5: 
        print("\nYour inventory is full. You must replace an item to equip this one.")
        print("Current inventory:")
            
        index = 1 
        for item in inventory.inv:
            print(f"{index}. {item.name} (STR: {item.STR}, HP: {item.HP})")
            index += 1
        
        print(f"\nThe chest contains: {random_item.name} (STR: {random_item.STR}, HP: {random_item.HP} ")

        while True: 
            choice = input("Do you want to replace an item? Enter the number of the item you want to replace, or press [N] to leave the chest.")
            if choice.lower() == "n": 
                print("You left the item.")
            else: 
                choice = int(choice) -1 
                if choice >= 0 and choice <= 5: 
                    print(f"You replaced {inventory.inv[choice].name} with {random_item.name}")
                    inventory.inv[choice] = random_item
                else: 
                    print("Invalid choice. you have to choose a number within your inventory, [1] - [5]")
    else: 
        C = input("Do you want to equip this item? [Y] or [N]\n")
        if C == "Y" or C == "y": 
            print("You picked up the item!")
            inventory.inv.append(random_item)
            classes.p1.STR += random_item.STR
            classes.p2.STR += random_item.STR
            classes.p1.HP += random_item.HP
            classes.p2.HP += random_item.HP
            


        elif C == "N" or C == "n": 
            print("You leave the item")
            
        else: 
            print("You have to choose [Y] or [N]!") 


def door_choice(): 
    global door_alternatives
    chosen_alternative = None #<-- detta ger den ett standardvärde vilket gör så att även om spelaren skriver in annat än "1, 2 eller 3" så kraschar inte spelet.

    door = (input("You have come to 3 doors. You will now either get to open a chest, fight a monster or encounter a trap!\nChoose one of the 3 doors.\n[1]LEFT\n[2]FORWARD\n[3]RIGHT\n"))
    # try:
    if door == "1" or door == "left" or door == "Left":  
        chosen_alternative = rand.choice(door_alternatives) 
        print("You have now encountered a", chosen_alternative)
    elif door == "2" or door == "middle" or door == "Middle": 
        chosen_alternative = rand.choice(door_alternatives) 
        print("You have now encountered a", chosen_alternative)
    elif door == "3" or door == "right" or door == "Right": 
        chosen_alternative = rand.choice(door_alternatives) 
        print("You have now encountered a", chosen_alternative)
    else: 
        print("There are only three doors, choose either [1], [2] or [3]!")

    if chosen_alternative == "Trap": 
        # Slumpa fram en skada mellan 5 och 20 HP
        damage = rand.randint(4, 20)
        classes.selected_player.take_damage(damage)
    elif chosen_alternative == "Monster": 
        print("Prepare for battle!")
        enemy_encounter() 

    elif chosen_alternative == "Chest":    
        print("You found a chest!") 
        print(f"It contains a {get_random_chest_item()}") 
        add_random_item()
    # except: 
    #     print("There is only three doors! Choose either [1], [2] or [3]\n")

    # def door_encounter():#skapar en funktion som bestämmer vad som händer när man möter trap, monster eller chest

