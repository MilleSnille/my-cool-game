import classes 
import random as rand
import inventory

door_alternatives = ["infested room", "burning room", "Monster", "Chest" ] 
# chosen_alternative = random.choice(door_alternatives) 

def get_random_enemy(): 
    global random_enemy
    enemy_types = [
        classes.enemy("ZOMBIE", 100, 5),
        classes.enemy("SCOBBY DOO", 55, 20),
        classes.enemy("DIDDY", 150, 50),
        classes.enemy("Terminator", 200, 100)
    ]
    random_enemy = rand.choice(enemy_types)
    return random_enemy
    

def enemy_encounter(): 
    global random_enemy
    print(f"You encounter {get_random_enemy()}")
    flee_or_fight = input(f"you've still got time to Flee! But remember, if you don't fight {random_enemy.name}, you might not get out of here!\n[1]Fight\n[2]Flee") 
    if flee_or_fight == "1" or flee_or_fight == "Fight" or flee_or_fight == "fight": 
        enemy_hp_damage = rand.randint(10,20)
        if classes.selected_player.HP / random_enemy.STR < random_enemy.HP / classes.selected_player.STR: 
            classes.p1.HP -= enemy_hp_damage
            classes.p2.HP -= enemy_hp_damage
            print(f"{random_enemy.name} was stronger than you! You lost {enemy_hp_damage} HP.")
        elif classes.selected_player.HP / random_enemy.STR > random_enemy.HP / classes.selected_player.STR: 
            print(f"Congratulations! You were stronger than {random_enemy.name}")
            classes.p1.LVL += 1
            classes.p2.LVL += 1
            print(f"You defeated the monster and leveled up to LVL:{classes.selected_player.LVL}")
        else: 
            print(f"You and {random_enemy.name} were evenly strong. {random_enemy.name} fled!")
    elif flee_or_fight == "2" or flee_or_fight =="Flee" or flee_or_fight == "flee":  
        print(f"You escaped {random_enemy.name}")



def get_random_chest_item():
    global random_item
    chest_items = [
        classes.item("Dissecting Set", 10, 0),
        classes.item("Acid bottle", 15, 0),
        classes.item("Mop", 8, 0),
        classes.item("Glass Shard", 12, 0),
        classes.item("Energy Sword", 25, 0),
        classes.item("Fire Flower", 20, 0),
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
            choice = input("Do you want to replace an item? Enter the number of the item you want to replace, or press [N] to leave the item.")
            if choice.lower() == "n": 
                print("You left the item behind.")
                return
            else: 
                choice = int(choice) -1 
                if choice >= 0 and choice <= 5: 
                    print(f"You replaced {inventory.inv[choice].name} with {random_item.name}")
                    inventory.inv[choice] = random_item
                    return
                else: 
                    print("Invalid input. You have to choose a number within your inventory, [1] - [5]")
    else: 
        C = input("Do you want to take this item with you? [Y] or [N]\n")
        if C == "Y" or C == "y": 
            print("You picked up the item!")
            inventory.inv.append(random_item)
            classes.p1.STR += random_item.STR
            classes.p2.STR += random_item.STR
            classes.p1.HP += random_item.HP
            classes.p2.HP += random_item.HP
            classes.p1.LVL += 1 
            classes.p2.LVL += 1
            print(f"you leveled up to LVL:{classes.selected_player.LVL}")
            
        elif C == "N" or C == "n": 
            print("You leave the item behind and journey forth")
        else: 
            print("You have to pick; [Y] or [N]!") 


def door_choice(): 
    global door_alternatives
    chosen_alternative = None #<-- detta ger den ett standardvärde vilket gör så att även om spelaren skriver in annat än "1, 2 eller 3" så kraschar inte spelet.

    door = (input("You have come to a crossroads with 3 doors. You may proceed into the unknown... \n(Enter one of the 3 doors.)\n[1]LEFT\n[2]FORWARD\n[3]RIGHT\n"))
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

    if chosen_alternative == "burning room": 
        # Slumpa fram en skada mellan 5 och 20 HP
        damage = rand.randint(4, 20)
        classes.selected_player.take_damage(damage)
    elif chosen_alternative == "infested room":
        damage = rand.randint(2, 15)
        classes.selected_player.take_damage(damage)
    elif chosen_alternative == "Monster": 
        print("Try and Survive!")
        enemy_encounter() 
    elif chosen_alternative == "Chest":    
        print("You found a Chest!") 
        print(f"It contains a {get_random_chest_item()}") 
        add_random_item()

    # def door_encounter():#skapar en funktion som bestämmer vad som händer när man möter trap, monster eller chest

